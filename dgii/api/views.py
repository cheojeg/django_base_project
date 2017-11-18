from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from dgii.models import Marbete
from .serializers import MarbeteSerializer
from rest_framework import status


class ActionListAPIView(APIView):

    def get(self, request, **kwargs):
        license_plate = self.kwargs['license_plate']
        marbete_query = Marbete.objects.filter(license_plate=license_plate)
        if marbete_query.exists():
            marbete = MarbeteSerializer(marbete_query, many=True)
            return Response({'data': marbete.data[0], 'status': 'OK'})
        else:
            msg = {'status': 'NOT FOUND'}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
