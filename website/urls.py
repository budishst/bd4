
from django.urls import path
 
# importing views from views..py
from .views import geeks_view
 
urlpatterns = [
    path('', views.home_view, name='home_view'),
]