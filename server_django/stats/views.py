from django.shortcuts import render
from rest_framework import viewsets

from .models import StatsModel
from .serializers import StatsSerializers


class StatsViewSet(viewsets.ModelViewSet):
    queryset = StatsModel.objects.all()
    serializer_class = StatsSerializers
