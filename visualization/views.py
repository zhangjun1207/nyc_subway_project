from django.shortcuts import render

# Create your views here.
def visualization(request):
    return render(request, 'visualization.html')