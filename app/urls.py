from django.urls import path
from app.views import TaskListView, TaskDetailView , TaskCreateView

urlpatterns=[
    path("tasklist/",TaskListView.as_view(), name='tasklist'),

    path("<int:pk>/",TaskDetailView.as_view(), name='task-detail'),

    path("task-create>/",TaskCreateView.as_view(), name='task-create')


]


app_name = "app"