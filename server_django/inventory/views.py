from django.shortcuts import render
from rest_framework import viewsets


from .models import InventoryModel
from .serializers import InventorySerializers


class InventoryViewSet(viewsets.ModelViewSet):
    queryset = InventoryModel.objects.all()
    serializer_class = InventorySerializers
