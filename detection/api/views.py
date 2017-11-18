from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.authtoken.models import Token
from dgii.models import Marbete
from agents.models import Agent
from .serializers import DetectionSerializer
from detection.models import Detection
from core.models import Log


class DectectionAPIView(APIView):

    def get(self, request, **kwargs):
        try:
            Log.objects.create_log_record('DectectionAPIView', request)
            try:
                uuid = self.kwargs['uuid']
            except Exception:
                uuid = None
            if uuid:
                detection_query = Detection.objects.filter(uuid=uuid)
            else:
                agent_query = Agent.objects.filter(
                    user_account_id=request.user)
                agent_id = agent_query[0]
                detection_query = Detection.objects.filter(agent_id=agent_id)
            if detection_query.exists():
                detection = DetectionSerializer(detection_query, many=True)
                return Response({'data': detection.data, 'status': 'OK'})
            else:
                msg = {'status': 'NOT FOUND'}
                return Response(msg, status=status.HTTP_404_NOT_FOUND)
        except Exception:
            msg = {'status': 'INTERNAL SERVER ERROR'}
            return Response(msg, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, **kwargs):
        try:
            Log.objects.create_log_record('DectectionAPIView', request)
            uuid = self.kwargs['uuid']
            detection_query = Detection.objects.filter(uuid=uuid)
            photo = request.data.get('photo')
            if detection_query.exists() and uuid and photo:
                detection = detection_query[0]
                detection.photo = photo
                detection.fined = True
                marbete_query = Marbete.objects.filter(
                    uuid=detection.marbete_id.uuid)
                marbete = marbete_query[0]
                marbete.penalized = True
                marbete.save()
                detection.save()
                detection = DetectionSerializer(detection_query, many=True)
                return Response({'data': detection.data[0], 'status': 'OK'})
            elif not latitude or not longitude:
                msg = {'status': 'BAD REQUEST'}
                return Response(msg, status=status.HTTP_404_NOT_FOUND)
            else:
                msg = {'status': 'NOT FOUND'}
                return Response(msg, status=status.HTTP_404_NOT_FOUND)
        except Exception:
            msg = {'status': 'INTERNAL SERVER ERROR'}
            return Response(msg, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
