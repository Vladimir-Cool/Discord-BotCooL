from django.shortcuts import render
from rest_framework import generics

from commands.models import CommandsModel
from commands.serializers import CommandsSerializer, CommandsEmbedSerializer


class CommandsAPIView(generics.ListAPIView):
    serializer_class = CommandsEmbedSerializer

    def get_queryset(self):
        name = self.kwargs.get("name")
        if name:
            return CommandsModel.objects.select_related().filter(name=name)

        return CommandsModel.objects.select_related().all()
