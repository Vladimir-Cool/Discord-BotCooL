from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.request import Request


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
        print(request.data)

        super().destroy(request, *args, **kwargs)


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
