from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth 

# Create your views here.
def signup(request):
 if request.method=='POST':
     if request.POST['password1']==request.POST['password2']:
         print("fuck fuck*****************************")
         try:
             user=User.objects.get(username=request.POST['username'])
             return render(request,'accounts/signup.html',{'error':'username has been taken'})
         except User.DoesNotExist:
             user= User.objects.create_user(username = request.POST['username'],password=request.POST['password1'])
             auth.login(request,user)
             #return redirect('home')
             #print("fuck")
             return render(request,'products/home.html')      
     else:
         return render(request,'accounts/signup.html',{'error':'you didint confirm password correctly!'})

        
 return render(request,'accounts/signup.html')   

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'] ,password=request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return render(request,'products/home.html')      
        else:
            return render(request,'accounts/login.html',{'error':'username or password maybe false'})   
    else:        
        return render(request,'accounts/login.html')   

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return render(request,'accounts/login.html')  
    else:
        return render(request,'accounts/login.html')   