from rest_framework import serializers
from detection.models import Detection
from dgii.api.serializers import MarbeteSerializer


class DetectionSerializer(serializers.ModelSerializer):
    agent_id = serializers.StringRelatedField(many=False)
    created = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S",
                                        required=False,
                                        read_only=True)
    modified = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S",
                                         required=False,
                                         read_only=True)
    marbete_id = MarbeteSerializer(many=False, read_only=True)

    class Meta:
        model = Detection
        fields = ('uuid', 'agent_id', 'marbete_id', 'latitude', 'longitude',
                  'photo', 'fined', 'created', 'modified')
