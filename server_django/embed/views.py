from django.shortcuts import render
from rest_framework import generics, viewsets, views
from embed.models import EmbedModel
from embed.serializers import EmbedSerializer


class EmbedAPIView(generics.ListAPIView):
    serializer_class = EmbedSerializer

    def get_queryset(self):
        name = self.kwargs.get("name")
        print(name)
        if name:
            return EmbedModel.objects.filter(name=name)

        return EmbedModel.objects.all()
