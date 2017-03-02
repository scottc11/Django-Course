from django.shortcuts import render
from .models import About

# Create your views here.
def about(request):
    return render(request, 'sitepages/about.html')
