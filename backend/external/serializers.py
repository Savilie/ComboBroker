from rest_framework import serializers


class INNSerializer(serializers.Serializer):
    inn = serializers.CharField()
