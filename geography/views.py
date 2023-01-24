from django.shortcuts import render
# Create your views here.

def geography(request):
    return render(request, 'geography/geography.html')