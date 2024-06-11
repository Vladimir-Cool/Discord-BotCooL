import io

from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from .models import User
from characters.serializers import CharactersSerializers
from inventory.serializers import InventorySerializers


class UserSerializer(serializers.ModelSerializer):
    """Сериализация для модели User"""

    class Meta:
        model = User
        fields = [
            "name",
            "discord_id",
            "experience",
            "inventory",
            "characters_count",
            "characters",
        ]
        extra_kwargs = {
            "experience": {"read_only": True},
            "characters_count": {"read_only": True},
            "characters": {"read_only": True},
            "inventory": {"read_only": True},
        }


class UserCharactersSerializer(UserSerializer):
    """Сериализация для модели User и связанной модели CharacterModel"""

    characters = CharactersSerializers(many=True, read_only=True)

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        return representation


class UserFullSerializer(UserSerializer):
    """Класс для вывода полного объекта пользователь со всеми связанными с ним объектами"""

    characters = CharactersSerializers(many=True, read_only=True)
    inventory = InventorySerializers(read_only=True)

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        return representation


# class UserModel:
#     """Класс модели для демонстрации серриализации"""
#
#     def __init__(self, name, discord_id):
#         self.name = name
#         self.discord_id = discord_id

# class UserSerializer(serializers.Serializer):
#     """ Класс сериализации для класса User"""
#     name = serializers.CharField(max_length=255)
#     discord_id = serializers.IntegerField(read_only=True)
#     experience = serializers.IntegerField(default=0)
#     last_activity_time = serializers.DateTimeField(read_only=True)
#     registration_date = serializers.DateTimeField(read_only=True)
#
#     def create(self, validated_data):
#         return User.objects.create(**validated_data)
#
#
#     def update(self, instance: User, validated_data):
#         instance.name = validated_data.get("name", instance.name)
#         instance.experience = validated_data.get("experience", instance.experience)
#         instance.save()
#         return instance


# class Meta:
#     model = User
#     fields = ("name", "experience", "discord_id")


# def encode():
#     """ Кодирование данный в JSON"""
#     model = UserModel("Gurtas", "15")
#     model_sr = UserSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep="\n")
#     json = JSONRenderer().render(model_sr.data)
#     print(json)


# def decode():
#     """ Декодирование данных из JSON формата"""
#     stream = io.BytesIO(b'{"discord_id":14,"name":"Monliter","experience":0}')
#     data = JSONParser().parse(stream)
#     serializer = UserSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)
