from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout 

from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def  base(request):
    return render(request,'base.html')
def login(request):
  
    if request.method=='POST':
         name=request.POST.get('name')
         password1=request.POST.get('password')

     
         user=authenticate(request,name=name,password=password1)
         
       
         if user is not None:
             login(request,user)
             return redirect(base)
         else:
             messages.info(request,'user not exists')
             print ('user not exists')
             return redirect(login)
         
    return render(request,'signin.html')


def signup(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        password1=request.POST.get('passwrd1')
        password2=request.POST.get('passwrd2')

       
        if password1 == password2:

            if User.objects.filter(username=name,email=email).exists():
                messages.info(request,'username already exist')
                print ("already have")
            else:
                new_user=User.objects.create_user(name,email,password1)
                new_user.save()
                return redirect(login)
        else:
            print('wrong password')        
    return render(request,'signup.html')


def logout(request):
    logout(request)
    return redirect(login)
def shop(request):
        return render(request,'product.html')
def cart(request):
    return render (request,'cart.html')