from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def latest_vacancies(request):
    return render(request, 'latestvacancies/latestvacancies.html')