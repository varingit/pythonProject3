from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'app/index.html')

def LWdp(request):
    return render(request, 'app/LWdp.html')

def MWdp(request):
    return render(request, 'app/MWdp.html')

def GWdp(request):
    return render(request, 'app/GWdp.html')