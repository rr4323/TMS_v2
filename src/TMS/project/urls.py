
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import ProjectApiViewSet,ProjectProgressApiViewSet

router = DefaultRouter()
router.register(r'', ProjectApiViewSet)

urlpatterns = [
    path('',include(router.urls) ),
    path("<int:id>/progress/",ProjectProgressApiViewSet.as_view({"get":"retrieve"}),name="project_progress")
]
