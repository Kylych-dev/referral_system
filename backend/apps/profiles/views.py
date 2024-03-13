from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.http import Http404

from .models import Profile
from .serializers import ProfileSerializer


class RefCodeModelViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticated,)


    @swagger_auto_schema(
        method="post",
        operation_description="Создание реферального кода",
        operation_summary="Создание реферального кода",
        tags=["Referal Code"],
        responses={
            201: openapi.Response(description="Created - Элемент успешно создан"),
            400: openapi.Response(description="Bad Request - Неверный запрос"),
        },
    )
    @action(detail=True, methods=["post"])
    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        except Exception as ex:
            return Response(
                {"Сообщение": str(ex)},
                status=status.HTTP_400_BAD_REQUEST
            )


    @swagger_auto_schema(
        method="delete",
        operation_description="Удаление реферального кода",
        operation_summary="Удаление реферального кода",
        tags=["Referal Code"],
        responses={
            204: openapi.Response(description="No Content - Элемент успешно удален"),
            404: openapi.Response(description="Not Found - Ресурс не найден"),
        },
    )
    @action(detail=True, methods=["delete"])
    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
        except Http404:
            return Response(
                {"Сообщение": "реферальный код не найден"},
                status=status.HTTP_404_NOT_FOUND
            )
        return Response(status=status.HTTP_204_NO_CONTENT)
