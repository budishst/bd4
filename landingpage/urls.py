from django.urls import path
from . import landingpage.views

urlpatterns = [
    path('', views.home_view, name='index'),
]
