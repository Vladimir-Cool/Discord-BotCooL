from django.forms import model_to_dict
from django.http import Http404
from django.shortcuts import render
from django.db import transaction
from rest_framework import viewsets, generics, status
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser

from .models import User
from .serializers import UserSerializer, UserCharactersSerializer, UserFullSerializer
from .permissions import IsAdminOrReadOnly
from inventory.serializers import InventorySerializer, InventoryFullSerializer, SlotSerializer
from inventory.models import InventoryModel

class UserViewSet(viewsets.ModelViewSet):
    # queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        """Метод который переопределяет поведение queryset для выборки объектов"""
        pk = self.kwargs.get("pk")
        if not pk:
            return User.objects.all()
        return User.objects.filter(discord_id=pk)  # filter

    @action(methods=["get"], detail=True)
    def get_exp(self, request, pk):
        """Возвращает опыт пользователя"""
        user = User.objects.get(discord_id=pk)
        return Response(
            {
                "name": user.name,
                "level": f"{int(user.experience // 100)} Уровень",
                "experiance": f"{user.experience % 100}%",
            }
        )

    # @action(methods=["get"], detail=True)
    # def get_user_char(self, request, pk):
    #     """Возвращает список персонажей"""
    #     characters =

    @action(methods=["get"], detail=True)
    def get_user(self, request, pk):
        """Возвращает пользователя и его персонажей"""
        user = User.objects.get(discord_id=pk)
        characters = user.characters.all()

        return Response(characters)

    @action(methods=["post"], detail=True)
    def registration(self, request, discord_id):
        """Регистрирует нового пользователя"""
        new_user = User(discord_id=discord_id)


class UserCharacterAPIList(generics.ListCreateAPIView):
    """Просмотр пользователя и его персонажей"""

    # queryset = User.objects.prefetch_related("characters").all()
    serializer_class = UserCharactersSerializer

    def get_queryset(self):
        """Метод который переопределяет поведение queryset для выборки объектов"""
        pk = self.kwargs.get("pk")
        if pk:
            user = User.objects.prefetch_related("characters").filter(discord_id=pk)
            return user

        return User.objects.prefetch_related("characters").all()

    def create(self, request: Request, *args, **kwargs):
        name = request.data["name"]

        with transaction.atomic():
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user_obj = serializer.save()

            # Создаем инвентарь для пользователя
            serializer_inventory = InventorySerializer(
                data={
                    "name": f"Инвентарь {name}",
                    "user": serializer.data["discord_id"],
                }
            )
            serializer_inventory.is_valid(raise_exception=True)
            inventory_obj: InventoryModel = serializer_inventory.save()
            
            # Создаем слоты в инвенторе
            list_slot_obj = [] # это не обязательно, собирать слоты в список?
            for i in range(inventory_obj.size + inventory_obj.extra_size):
                print(f"Это ш - {i}")
                serializer_slot = SlotSerializer(data={
                    "inventory": serializer_inventory.data["id"]
                })
                serializer_slot.is_valid(raise_exception=True)
                slot_obj = serializer_slot.save()
                list_slot_obj.append(slot_obj) # это не обязательно, подумать надо ли это?

        user_obj.refresh_from_db()
        # inventory_obj.refresh_from_db()

        serializer_2: UserFullSerializer = UserFullSerializer(user_obj)

        return Response(serializer_2.data, status=status.HTTP_201_CREATED)


""" Тестовые приколы"""


class UserAPIList(generics.ListCreateAPIView):
    """API Класс для GET и POST запросов"""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class UserAPIUpdate(generics.RetrieveUpdateAPIView):
    """API Класс для PUT и PATH запросов"""

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserAPIDestroy(generics.RetrieveDestroyAPIView):
    """API Класс для CRUD"""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminOrReadOnly,)


class UserAPIView(APIView):
    """класc с описанием методов для примера
    НЕ используется"""

    def get(self, request):
        u = User.objects.all()
        return Response({"users": UserSerializer(u, many=True).data})

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})

    def put(self, request, *arg, **kwargs):
        discord_id = kwargs.get("discord_id", None)
        if not discord_id:
            return Response({"error": "Method put not allowed"})
        try:
            instance = User.objects.get(discord_id=discord_id)
        except User.DoesNotExist:
            return Response({"error": "Object does not exist"})

        serializer = UserSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})

    def delete(self, request, *arg, **kwargs):
        discord_id = kwargs.get("discord_id", None)
        if not discord_id:
            return Response({"error": "Method put not allowed"})
        try:
            instance = User.objects.get(discord_id=discord_id)
        except User.DoesNotExist:
            return Response({"error": "Object does not exist"})
        instance.delete()
        return Response({"delete": f"Удален пользователь discord_id={discord_id}"})
