from rest_framework.routers import SimpleRouter
from apps.core import views

router = SimpleRouter()

router.register(r'settings', views.PageSettingViewSet)
router.register(r'pages', views.PageViewSet)

urlpatterns = router.urls
