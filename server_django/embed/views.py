import json

from django.shortcuts import render, HttpResponse
from django.template import Context, Template
from rest_framework import generics, viewsets, views
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer

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


class EmbedUserView(generics.ListCreateAPIView):
    serializer_class = EmbedSerializer

    def get_queryset(self):
        name = self.kwargs.get("name")
        print(name)
        if name:
            return EmbedModel.objects.filter(name=name)

        return None

    def embed_render(self, template: str, context_data: dict):
        """Значения поля fields должно быть строкой.
        ковычки экранируем -\"
        списки обрамляем ковычками - "[]"
        """
        template_instance = Template(template)
        print(context_data)
        context = Context(context_data)

        result_render = template_instance.render(context)

        # print(result_render)

        result_json = json.loads(result_render)

        # print("-1-")
        # print(result_json)

        if "fields" in result_json.keys():
            result_json["fields"] = json.loads(result_json["fields"][:-2] + "]")
            # -->[:-2] + "]"<-- Это я ',' убираю которая появилась в результате рендеринга

        # print("-2-")
        # print(result_json)

        return result_json

    def post(self, request, *args, **kwargs):
        embed_name = request.data["embed_name"]
        embed_obj = EmbedModel.objects.filter(name=embed_name).first()
        embed_sr = EmbedSerializer(embed_obj)

        json = self.embed_render(embed_sr.data["embed_template"], request.data)

        return Response(json)
