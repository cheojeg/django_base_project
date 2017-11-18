from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.authtoken.models import Token
from dgii.models import Marbete
from agents.models import Agent
from .serializers import MarbeteSerializer
from detection.models import Detection
from core.models import Log


class MarbeteAPIView(APIView):

    def get(self, request, **kwargs):
        try:
            Log.objects.create_log_record('MarbeteAPIView', request)
            license_plate = self.kwargs['license_plate']
            marbete_query = Marbete.objects.filter(license_plate=license_plate)
            latitude = self.request.query_params.get('latitude', None)
            longitude = self.request.query_params.get('longitude', None)
            if latitude and longitude:
                latitude = float(latitude)
                longitude = float(longitude)
            if marbete_query.exists() and isinstance(latitude, float) and \
                    isinstance(longitude, float):
                agent_query = Agent.objects.filter(
                    user_account_id=request.user)
                detection_data = {}
                detection_data['agent_id'] = agent_query[0]
                detection_data['marbete_id'] = marbete_query[0]
                detection_data['latitude'] = latitude
                detection_data['longitude'] = longitude
                detection_data['fined'] = None
                Detection.objects.create_detection(detection_data)
                marbete = MarbeteSerializer(marbete_query, many=True)
                return Response({'data': marbete.data[0], 'status': 'OK'})
            elif not latitude or not longitude:
                msg = {'status': 'BAD REQUEST'}
                return Response(msg, status=status.HTTP_404_NOT_FOUND)
            else:
                msg = {'status': 'NOT FOUND'}
                return Response(msg, status=status.HTTP_404_NOT_FOUND)
        except Exception:
            msg = {'status': 'INTERNAL SERVER ERROR'}
            return Response(msg, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
