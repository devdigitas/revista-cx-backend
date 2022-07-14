from rest_framework.routers import SimpleRouter
from apps.core import views

router = SimpleRouter()

router.register(r'pages', views.PageViewSet)

urlpatterns = router.urls
