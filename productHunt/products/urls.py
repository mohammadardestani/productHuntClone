
from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('create/',views.create,name='create'),
    path('<int:product_id>',views.product_detail,name='product_detail'),
    path('<int:product_id>/upvote',views.upvote,name= 'upvote'),
    
 
]
