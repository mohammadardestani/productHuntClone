from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Product
from django.utils import timezone
# Create your views here.
@login_required
def create(request):
    if request.method=='POST':
      
        print("first step **********************************************")
        if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['icon'] and request.FILES['image']:
            print("second step **********************************")
            product = Product()
            product.title = request.POST['title']
            product.body = request.POST['body']
            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
                product.url =  request.POST['url']
            else:
                product.url =  'http://' + request.POST['url']

            product.icon= request.FILES['icon']
            product.image  =  request.FILES['image']
            product.hunter = request.user
            product.pup_date= timezone.datetime.now()
            product.save()
            return render(request,'products/home.html')
            #return redirect ('home')
        else:
            return render(request,'products/create.html',{'error':"you most fill all the fields"})
    else:
             return render(request,'products/create.html')


def home(request):
    return render(request,'products/home.html')
   
