from django.shortcuts import render

# Create your views here.
def exploratory_1(request):
    return render(request, 'exploratory_analysis_1.html')

def exploratory_2(request):
    return render(request, 'exploratory_analysis_2.html')