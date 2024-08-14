
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import TaskApiViewSet,TaskAssignApiViewSet, TaskCommentDeleteApiViewSet, TaskCommentsApiViewSet, TaskCompleteApiViewSet, TaskOverDueApiViewSet,TaskUnAssignApiViewSet

router = DefaultRouter()
router.register(r'', TaskApiViewSet)

urlpatterns = [
    path('',include(router.urls) ),
    path('<int:id>/comments/', TaskCommentsApiViewSet.as_view({'post': 'create','get':'list'}, name="create_retrieve_comment")),
    path('<int:id>/assign/', TaskAssignApiViewSet.as_view({'post': 'create'}), name='task_assign'),
    path('<int:id>/unassign/', TaskUnAssignApiViewSet.as_view({'post': 'create'}), name='task_unassign'),
    path('<int:id>/complete/', TaskCompleteApiViewSet.as_view({'put': 'update'}), name='task_complete'),
    #for custom url
    path('<int:task_id>/comments/<int:comment_id>/',TaskCommentDeleteApiViewSet.as_view({'delete': 'destroy'}), name='delete_comment'),
    
]
