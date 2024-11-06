from django.shortcuts import render

from django.views.generic import ListView, DetailView, CreateView

from app.models import Task

from app.forms import TaskForm

from django.urls import reverse_lazy
class TaskListView(ListView):
    model = Task
    template_name = "ListOfTusks.html"
    context_object_name = "Tasks"

class TaskDetailView(DetailView):
    model = Task
    template_name = "DetailOfTask.html"
    context_object_name = "task"


class TaskCreateView(CreateView):
    model = Task
    templste_name = "TaskCreate.html"
    seccess_url=reverse_lazy("ListOfTusks")
    form_class = TaskForm
