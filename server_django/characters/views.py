from django.shortcuts import render
from rest_framework import viewsets, generics, status
from rest_framework.request import Request
from rest_framework.response import Response

from .models import CharactersModel
from .serializers import CharactersSerializers


class CharactersViewSet(viewsets.ModelViewSet):
    queryset = CharactersModel.objects.all()
    serializer_class = CharactersSerializers
    lookup_field = "name"  # Изменяет параметр поиска на name

    # def get_queryset(self, discord_id, name):
    #     """Метод который переопределяет поведение queryset для выборки объектов"""
    #     discord_id = self.kwargs.get("discord_id")
    #     name = self.kwargs.get("name")
    #     if not discord_id and not name:
    #         return CharactersModel.objects.all()
    #     return CharactersModel.objects.filter(discord_id=discord_id, name=name)
    def destroy(self, request: Request, *args, **kwargs):
        # тут надо дернуть персонажа из БД и проверить га соответствеи пользователю.
        # Пользователя id надо передать
        print(request.data)

        instance = self.get_object()
        print(instance.user.discord_id)
        if instance.user.discord_id == request.data["discord_id"]:
            self.perform_destroy(instance)
            serializer = self.get_serializer(instance)
            return Response(status=status.HTTP_204_NO_CONTENT, data=serializer.data)
        return Response(status=status.HTTP_403_FORBIDDEN)


class CharactersViewList(generics.ListCreateAPIView):
    serializer_class = CharactersSerializers

    def get_queryset(self):
        """
        Метод который переопределяет поведение queryset для выборки объектов.
        Возвращает персонажа по указанному user_id и .name
        """
        user = self.kwargs.get("pk")
        name = self.kwargs.get("name")
        if user and name:
            return CharactersModel.objects.filter(user=user, name=name)
        elif user and not name:
            return CharactersModel.objects.filter(user=user)
