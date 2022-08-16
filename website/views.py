from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_view(request):
 
    # logic of view will be implemented here
    return render(request, "landingpage/templates/home.html")