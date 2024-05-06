from rest_framework import serializers

from embed.models import EmbedModel


class EmbedSerializer(serializers.ModelSerializer):

    class Meta:
        model = EmbedModel

        fields = (
            "name",
            "embed_template",
            "embed_enabled"
        )
        
        # extra_kwargs = {}
