from rest_framework import serializers


class MatrixSerializer(serializers.Serializer):
    size = serializers.IntegerField()
    matrix = serializers.ListField(child=serializers.ListField(child=serializers.FloatField()))
    invertedMatrix = serializers.ListField(child=serializers.ListField(child=serializers.FloatField()))

class PillowImageSerializer(serializers.Serializer):
    image_base64 = serializers.CharField()
    encoding = serializers.CharField()