from rest_framework import serializers
from detection.models import Detection


class DetectionSerializer(serializers.ModelSerializer):
    agent_id = serializers.StringRelatedField(many=False)

    class Meta:
        model = Detection
        fields = ('uuid', 'agent_id', 'marbete_id', 'latitude', 'longitude',
                  'photo', 'fined')
