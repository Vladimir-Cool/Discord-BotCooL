from django.shortcuts import render
from rest_framework import generics, viewsets, views
from embed.models import EmbedModel
from embed.serializers import EmbedSerializer


class EmbedViewSet(generics.ListAPIView):
    serializer_class = EmbedSerializer

    def get_queryset(self):
        name = self.kwargs.get("name")
        print(name)
        if not name:
            return EmbedModel.objects.all()

        return EmbedModel.objects.filter(name=name)





