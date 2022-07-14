from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from apps.users import serializers
from apps.users import models
from apps.users.permissions import *
from rest_framework.permissions import IsAuthenticated


class UserViewSet(ModelViewSet):

    serializer_class = serializers.UserSerializer
    queryset = models.User.objects.all().exclude(pk=1)
    permission_classes = [IsAuthenticated]
    filter_fields = []
    search_fields = ['email', 'first_name']

    def retrieve(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)

        if pk == 'me':
            if not request.user.is_anonymous:
                user = models.User.objects.get(pk=request.user.id)
                return Response(self.serializer_class(user, context={'request': request}).data)
            else:
                return Response(
                    {'message': 'El usuario no esta autenticado para permitir este endpoint'},
                    status=status.HTTP_401_UNAUTHORIZED
                )

        return super().retrieve(request, *args, **kwargs)