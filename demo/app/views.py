from django.shortcuts import render

# Create your views here.



def home(request):
    return render(request,'index.html')
def abt(request):
    return render(request,'about.html')
def hm(request):
    return render(request,'home.html')