from rest_framework import serializers

from .models import CharactersModel


class CharactersSerializers(serializers.ModelSerializer):
    class Meta:
        model = CharactersModel
        fields = (
            "id",
            "name",
            "user",
            "level",
            "experience",
        )
        extra_kwargs = {
            "id": {"read_only": True},
            "level": {"read_only": True},
            "experience": {"read_only": True},
        }
