"""
URL configuration for server_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter


from user.views import (
    UserViewSet,
    UserCharacterAPIList,
    UserAPIList,
    UserAPIUpdate,
    UserAPIDestroy,
)
from characters.views import CharactersViewSet, CharactersViewList, CharactersDeleteView
from inventory.views import InventoryViewSet
from items.views import ItemsViewSet
from stats.views import StatsViewSet
from embed.views import EmbedAPIView, EmbedUserView
from commands.views import CommandsAPIView

router = DefaultRouter()
router.register(r"users", UserViewSet, basename="user")
router.register(r"characters", CharactersViewSet, basename="characters")
router.register(r"inventory", InventoryViewSet, basename="inventory")
router.register(r"items", ItemsViewSet, basename="items")
router.register(r"stats", StatsViewSet, basename="stats")
# router.register(r"embed", EmbedAPIView, basename="embed")


# print(router.urls)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include(router.urls)),
    path("api/v1/drf-auth/", include("rest_framework.urls")),
    path("api/v1/userswithchars/", UserCharacterAPIList.as_view()),
    path("api/v1/userswithchars/<int:pk>/", UserCharacterAPIList.as_view()),
    path("api/v1/userswithchars/create/", UserCharacterAPIList.as_view()),
    path("api/v1/userslist/", UserAPIList.as_view()),
    path("api/v1/userslist/<int:pk>/", UserAPIUpdate.as_view()),
    path("api/v1/usersdelete/<int:pk>/", UserAPIDestroy.as_view()),
    # Вернет персонажей по id User
    path("api/v1/usercharacters/<int:pk>/", CharactersViewList.as_view()),
    # Вернет персонажа по id User и name
    path("api/v1/characters/<int:pk>/<str:name>/", CharactersViewList.as_view()),
    path(
        "api/v1/characters/<int:user_id>/<str:name>/delete/",
        CharactersDeleteView.as_view(),
    ),
    # path("api/v1/charactersdelete/<int:pk>/<str:name>/", CharactersDelet.as_view())
    path("api/v1/embed/", EmbedAPIView.as_view()),
    path("api/v1/embed/<str:name>/", EmbedAPIView.as_view()),
    path("api/v1/command/", CommandsAPIView.as_view()),
    path("api/v1/command/<str:name>", CommandsAPIView.as_view()),
    path("api/v1/renderembed/", EmbedUserView.as_view()),
]
