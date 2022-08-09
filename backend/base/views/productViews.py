from email import message_from_string
import imp
from platform import java_ver
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from .products import products
from base.models import Product
from base.serializer import ProductSerializer




@api_view(['GET'])
#for list of products
def getProducts(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products,many = True)
    return Response(serializer.data) # needs to pass the object data



@api_view(['GET'])
#for single product
def getProduct(request,__id):
    product = Product.objects.get(_id = __id)
    serializer = ProductSerializer(product,many = False)
    return Response(serializer.data)