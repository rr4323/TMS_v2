
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import TaskApiViewSet

router = DefaultRouter()
router.register(r'', TaskApiViewSet)

urlpatterns = [
    path('',include(router.urls) ),
]
