from rest_framework.viewsets import ModelViewSet
from apps.core.serializers import *
from apps.core.models import *


class PageViewSet(ModelViewSet):

    queryset = Page.objects.all().order_by('page', 'name')
    serializer_class = PageSerializer

    filter_fields = ['isActive', 'page']
    ordering_fields = ['name']
    search_fields = ['name',]