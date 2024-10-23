from django.urls import path
from .views import TuskListView

urlpatterns=[
    path("",TuskListView.as_view(), name='tusklist')

]