from django.shortcuts import render
# Create your views here.

def demand(request):
    return render(request, 'demand/demand.html')