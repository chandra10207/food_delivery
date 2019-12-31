from django.core import exceptions
from django.shortcuts import render
from rest_framework.response import Response

from sales.models import Order
from sales.models import OrderItem
from sales.models import OrderItemMeta
from sales.serializers import OrderSerializer
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
        user_id = self.request.query_params.get('user_id')
        if user_id:
            if User.objects.filter(id=user_id).exists():
                queryset = Order.objects.filter(user_id=user_id)
            else:
                content = {'errors': 'user id not exist'}
                raise ValidationError(content)
        else:
            queryset = Order.objects.all()
        return queryset
    serializer_class = OrderSerializer


class OrderListDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


def index(request):
    return HttpResponse('Hello from Sales Index page!')


