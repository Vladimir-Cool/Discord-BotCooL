from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, generics, status
from rest_framework.request import Request
from rest_framework.response import Response

from .models import CharactersModel
from .serializers import CharactersSerializers


class CharactersViewSet(viewsets.ModelViewSet):
    queryset = CharactersModel.objects.all()
    serializer_class = CharactersSerializers
    lookup_field = "name"  # Изменяет параметр поиска на name


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


class CharactersDeleteView(generics.DestroyAPIView):
    """
    Класс для удаления персонажа с предварительной проверкой пользователя который удаляет.
    Пользователь может удалять только с воих персонажей.
    Но можно подделать URL и удалить персонажа !!! ЭТО НАДО ДУМАТЬ.
    """

    serializer_class = CharactersSerializers
    queryset = CharactersModel.objects.all()

    def get_object(self):
        """
        Переназначаю функцию
        для того чтобы фильтровать query_set по 2 параметрам:
        user_id: id пользователя
        name: имя персонажа
        """
        queryset = self.get_queryset()
        filter_kwargs = {
            "user_id": self.kwargs.get("user_id"),
            "name": self.kwargs.get("name"),
        }
        obj = get_object_or_404(queryset, **filter_kwargs)
        return obj

    def destroy(self, request: Request, *args, **kwargs):
        """Тут помимо статус кода мы вернем и сам удаленный объект"""
        instance = self.get_object()
        self.perform_destroy(instance)

        serializer = self.get_serializer(instance)
        return Response(serializer.data)
