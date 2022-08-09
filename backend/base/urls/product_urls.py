from django.urls import path

from base.views import productViews as views

urlpatterns = [
   
    path('',views.getProducts, name='products'),
    path('<str:__id>/',views.getProduct, name='product'),

]