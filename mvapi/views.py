from django.shortcuts import render
from django.core.serializers import serialize
from shop.models import Product
from django.http import HttpResponse

from rest_framework import viewsets
from shop.models import Product
from .serializers import ProductSerializer
from rest_framework.views import  APIView
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def pro(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def pro_details(request,pk):
    try:
        instance=Product.objects.get(id=pk)
    except Product.DoesNotExist:
        return HttpResponse(status=404)
    if request.method=='GET':
        serializer=ProductSerializer(instance=instance)
        return JsonResponse(serializer.data)

    elif request.method=="PUT":
        data=JSONParser().parse(request)
        serializer=ProductSerializer(instance,data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method=="DELETE":
        instance.delete()
        return HttpResponse(status=204)

