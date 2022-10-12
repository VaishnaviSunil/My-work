from django.shortcuts import render

# Create your views here.
def index (request):
    return render(request,'hall.html')

def home (request):
    return render (request,'home.html')

def fun (request):
    return render (request,'room.html')