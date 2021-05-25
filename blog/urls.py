from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home,name='blogHome'),
    path('blogpost/<int:id>', views.blogpost,name='blogPost'),

    ]