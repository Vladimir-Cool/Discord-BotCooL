from django.shortcuts import render
from django.db import transaction
from rest_framework import viewsets, generics, status
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request



from .models import InventoryModel
from .serializers import InventorySerializer, InventoryFullSerializer

class InventoryViewSet(viewsets.ModelViewSet):
    queryset = InventoryModel.objects.all()
    serializer_class = InventorySerializer

class InventoryListAPIView(generics.ListAPIView):
    serializer_class = InventoryFullSerializer
    # queryset = InventoryModel.objects.prefetch_related("slots").all()
    # lookup_field = "user"


    def get_queryset(self):
        """В принципе этот код дублирует функционал поле 'queryset' и 'lookup_field'
        Но его пока чт оставлю в целях понимания"""
        
        user = self.kwargs.get("user")
        if user:
            return InventoryModel.objects.prefetch_related("slots").filter(user=user)
        return InventoryModel.objects.prefetch_related("slots").all()


