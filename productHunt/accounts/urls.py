
from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('login',views.login,name='login'),
    path('signup',views.signup,name='signup'),
    path('logout',views.signup,name='logout'),
    
]
