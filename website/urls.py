from django.urls import path
from .views import geeks_view
 
urlpatterns = [
    path('', views.home_view, name='home_view'),
]