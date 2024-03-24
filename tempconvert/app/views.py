from django.shortcuts import render

# Create your views here.
def temperature_converter(request):
    return render(request,'index.html')