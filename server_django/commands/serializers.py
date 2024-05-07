from rest_framework.serializers import ModelSerializer

from commands.models import CommandsModel
from embed.serializers import EmbedSerializer


class CommandsSerializer(ModelSerializer):

    class Meta:
        model = CommandsModel

        fields = (
            "name",
            "description",
            "enabled",
            "embed",
        )


class CommandsEmbedSerializer(CommandsSerializer):
    embed = EmbedSerializer(many=False)
