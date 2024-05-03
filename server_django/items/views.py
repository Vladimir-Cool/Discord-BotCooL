from django.shortcuts import render
from rest_framework import viewsets

from .models import ItemsModel
from .serializers import ItemsSerializers


class ItemsViewSet(viewsets.ModelViewSet):
    queryset = ItemsModel.objects.all()
    serializer_class = ItemsSerializers
