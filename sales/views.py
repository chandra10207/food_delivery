from django.core import exceptions
from django.shortcuts import render
from rest_framework.response import Response

from sales.models import Order
from sales.models import OrderItem
from sales.models import OrderItemMeta
from sales.serializers import OrderSerializer, OrderDetailSerializer, OrderItemSerializer
from rest_framework import generics
from django.http import HttpResponse
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import ValidationError
# Create your views here.


class OrderListApi(generics.ListCreateAPIView):

    def get_queryset(self):
        params = self.request.query_params
        # breakpoint()
        user_id = params.get('user_id')
        status = params.get('order_status')
        if user_id and status:
            if User.objects.filter(id=user_id).exists():
                queryset = Order.objects.filter(user_id=user_id).filter(order_status=status).order_by('-id')

            else:
                content = {'errors': 'user id not exist'}
                raise ValidationError(content)

        elif user_id:
            if User.objects.filter(id=user_id).exists():
                queryset = Order.objects.filter(user_id=user_id).order_by('-id')
            else:
                content = {'errors': 'user id not exist'}
                raise ValidationError(content)

        elif status:
            if Order.objects.filter(order_status=status).exists():
                queryset = Order.objects.filter(order_status=status).order_by('-id')
            else:
                content = {'errors': 'Order status not exist'}
                raise ValidationError(content)
        else:
            queryset = Order.objects.all().order_by('-id')
        return queryset
    serializer_class = OrderSerializer


class OrderListDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderDetailSerializer


class OrderItemListApi(generics.ListCreateAPIView):

    def get_queryset(self):
        params = self.request.query_params
        # breakpoint()
        user_id = self.request.query_params.get('user_id')
        if user_id:
            if User.objects.filter(id=user_id).exists():
                queryset = Order.objects.filter(user_id=user_id).order_by('-id')
            else:
                content = {'errors': 'user id not exist'}
                raise ValidationError(content)
        else:
            queryset = OrderItem.objects.all().order_by('-id')
        return queryset
    serializer_class = OrderItemSerializer


class OrderItemDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderDetailSerializer


def index(request):
    return HttpResponse('Hello from Sales Index page!')


