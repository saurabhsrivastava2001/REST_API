from rest_framework import serializers

class MovieSerializer (serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=1000, allow_blank=True)
    active = serializers.BooleanField(default=True)
    