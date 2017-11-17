from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from dgii.models import Marbete
from .serializers import MarbeteSerializer


class ActionListAPIView(APIView):

    def get(self, request, **kwargs):
        action_list = Marbete.objects.all()
        action_list = MarbeteSerializer(action_list, many=True)
        action_list = action_list.data
        return Response({'data': action_list})
