from django.shortcuts import render

# Create your views here.
def predictive(request):
    return render(request, 'predictive.html')