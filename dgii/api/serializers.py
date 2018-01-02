from rest_framework import serializers
from dgii.models import Marbete, Code


class CodeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Code
        fields = ('code', 'description')


class MarbeteSerializer(serializers.ModelSerializer):
    code = CodeSerializer(many=False, read_only=True)
    created = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S",
                                        required=False,
                                        read_only=True)
    modified = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S",
                                         required=False,
                                         read_only=True)

    class Meta:
        model = Marbete
        fields = ('uuid', 'code', 'license_plate', 'brand', 'model',
                  'type_vehicle', 'year_production', 'amount', 'owner',
                  'document_description', 'document_type', 'oposition',
                  'valid', 'color', 'penalized', 'created', 'modified')
