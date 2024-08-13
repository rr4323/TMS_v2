
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import ProjectApiViewSet

router = DefaultRouter()
router.register(r'', ProjectApiViewSet)

urlpatterns = [
    path('',include(router.urls) ),
]
