from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product
from .models import Vote
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
            #return render(request,'products/home.html')
            return redirect ('/products/' + str(product.id))
        else:
            return render(request,'products/create.html',{'error':"you most fill all the fields"})
    else:
            return render(request,'products/create.html')

def product_detail(request,product_id):
    product = get_object_or_404(Product,pk=product_id)
    return render(request,'products/detail.html',{'product' : product})


def home(request):
    return render(request,'products/home.html')


def upvote(request,product_id):
    
    if request.method=='POST':
       product = get_object_or_404(Product,pk=product_id)
       user = request.user
       import pdb;pdb.set_trace()
       try:
            vote = Vote.objects.get(user=user , product=product)
            return redirect ('/products/' + str(product.id))  
       except Vote.DoesNotExist:
             vote= Vote.objects.create(user=user , product=product)
             product.votes_total +=1
             product.save()
             return redirect ('/products/' + str(product.id))  
    else:
         return render(request,'accounts/signup.html',{'error':'you didint confirm password correctly!'})

      # return redirect ('/products/' + str(product.id))
       
       

    
    
