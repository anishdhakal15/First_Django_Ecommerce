from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home,name='ShopHome'),
    path('about/', views.about,name='AboutUs'),
    path('contact/', views.contact,name='ContactUs'),
    path('tracker/', views.tracker,name='TrackingStatus'),
    path('search/', views.search,name='Search'),
    path('products/<int:myid>', views.productview,name='ProductView'),
    path('checkout/', views.checkout,name='CheckOut'),
    ]