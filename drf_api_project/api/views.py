from django.shortcuts import render
from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.serializers import ProductSerializer, OrderSerializer, OrderItemSerializer
from api.models import Product, Order, OrderItem

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/product-list/',
        'Detail View': '/product-detail/<str:pk>/',
        }

    return Response(api_urls)

# for products:
@api_view(['GET'])
def productList(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def productDetail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)




# for orders:
@api_view(['GET'])
def orderList(request):
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)