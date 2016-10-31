from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def data_preparation(request):
    return render(request, 'data_preparation.html')
