from rest_framework.viewsets import ModelViewSet
from apps.core.serializers import *
from apps.core.models import *
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class PageSettingViewSet(ModelViewSet):

    queryset = PageSetting.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PageSettingSerializer


class PageViewSet(ModelViewSet):

    queryset = Page.objects.all().order_by('page', 'name')
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PageSerializer

    filter_fields = ['isActive', 'page']
    ordering_fields = ['name']
    search_fields = ['name',]