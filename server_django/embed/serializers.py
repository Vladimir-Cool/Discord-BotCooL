# from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework import serializers

from embed.models import EmbedModel


class EmbedSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmbedModel

        fields = (
            "name",
            "embed_template",
            "embed_enabled",
        )

        # extra_kwargs = {}


class EmbedFieldsSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=90)
    value = serializers.CharField(max_length=400)
    inline = serializers.BooleanField()


class EmbedJSONSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=400)
    color = serializers.IntegerField()
    fields = EmbedFieldsSerializer(many=True, read_only=True)

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        return representation
