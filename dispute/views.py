from django.core import exceptions
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from django.http import HttpResponse
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import ValidationError

from dispute.models import Dispute
from dispute.serializers import DisputeSerializer, DisputeDetailSerializer

# Create your views here.


class DisputeListApi(generics.ListCreateAPIView):

    # def get_queryset(self):
    #     params = self.request.query_params
    #     # breakpoint()
    #     user_id = params.get('user_id')
    #     status = params.get('order_status')
    #     if user_id and status:
    #         if User.objects.filter(id=user_id).exists():
    #             queryset = Order.objects.filter(user_id=user_id).filter(order_status=status)
    #
    #         else:
    #             content = {'errors': 'user id not exist'}
    #             raise ValidationError(content)
    #
    #     elif user_id:
    #         if User.objects.filter(id=user_id).exists():
    #             queryset = Order.objects.filter(user_id=user_id)
    #         else:
    #             content = {'errors': 'user id not exist'}
    #             raise ValidationError(content)
    #
    #     elif status:
    #         if Order.objects.filter(order_status=status).exists():
    #             queryset = Order.objects.filter(order_status=status)
    #         else:
    #             content = {'errors': 'Order status not exist'}
    #             raise ValidationError(content)
    #     else:
    #         queryset = Order.objects.all()
    #     return queryset
    queryset = Dispute.objects.all()
    serializer_class = DisputeSerializer


class DisputeDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dispute.objects.all()
    serializer_class = DisputeDetailSerializer