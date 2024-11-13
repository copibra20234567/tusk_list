from django.urls import path, include
from app.views import TaskListView, TaskDetailView , TaskCreateView

app_name = "app"

urlpatterns=[
    path("app:tasklist",TaskListView.as_view(), name='tasklist'),

    path("<int:pk>/",TaskDetailView.as_view(), name='task-detail'),

    path("task-create>/",TaskCreateView.as_view(), name='task-create'),

    path('', include('app.urls', namespace='app'))

]


