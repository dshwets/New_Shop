from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from api_v1.serrializers import ProductSerializer, OrderSerializer
from webapp.models import Product, Order


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrderApi(APIView):
    def get(self,request,*args,**kwargs):
        print(request)
        order = get_object_or_404(Order, pk=kwargs.get('pk'))
        slr = OrderSerializer(order)
        return Response(slr.data)

    def post(self, request, *args, **kwargs):
        slr = OrderSerializer(data=request.data)
        if slr.is_valid():
            order = slr.save()
            return Response(slr.data)
        else:
            return Response(slr.errors, status=400)
