from django.shortcuts import render
from .models import Converter

# Create your views here.

def index(request):
    converters = Converter.objects.all()
    context = {
        'converters': converters
        }
    return render(request, 'converters/list.html', context)

def lengthconv(request):
    return render(request, 'calculators/lengthconv.html')

def capacityconv(request):
    return render(request, 'calculators/capacityconv.html')

def heatconv(request):
    return render(request, 'calculators/heatconv.html')

def exchangeconv(request):
    return render(request, 'calculators/exchangeconv.html')

