from rest_framework.serializers import ModelSerializer

from embed.models import EmbedModel


class EmbedSerializer(ModelSerializer):

    class Meta:
        model = EmbedModel

        fields = (
            "name",
            "embed_template",
            "embed_enabled",
        )
        
        # extra_kwargs = {}
