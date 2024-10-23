from django.shortcuts import render

from django.views.generic import ListView

from .models import Tusk



class TuskListView(ListView):
    model = Tusk
    template_name = "template/ListOfTusks.html"
    context_object_name = "Tusks"
