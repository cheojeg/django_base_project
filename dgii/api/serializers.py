from rest_framework import serializers
from dgii.models import Marbete


class MarbeteSerializer(serializers.ModelSerializer):
    code = serializers.StringRelatedField(many=False)

    class Meta:
        model = Marbete
        fields = ('uuid', 'code', 'license_plate', 'brand', 'model',
                  'type_vehicle', 'year_production', 'amount', 'owner',
                  'document_description', 'document_type', 'oposition',
                  'valid', 'penalized')
