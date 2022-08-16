from django.urls import path
from . import landingpage.views

urlpatterns = [
    path('', landingpage.views.home_view, name='index'),
]
