from rest_framework import serializers


class QuizSerializer(serializers.Serializer):
    number = serializers.CharField()
    type = serializers.CharField()
    price = serializers.IntegerField()
    vznos = serializers.IntegerField()
    program = serializers.CharField()
    city = serializers.CharField()


class FeedbackSerializer(serializers.Serializer):
    number = serializers.CharField()
    theme = serializers.CharField()
    messenger = serializers.CharField()

