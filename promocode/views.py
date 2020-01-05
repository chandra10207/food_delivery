# from django.shortcuts import render
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView

from promocode.models import Coupon
from promocode.serializers import CouponSerializer
from rest_framework import generics
from rest_framework.validators import ValidationError
from rest_framework import views as restframework_views
from django.http import HttpResponse


# Create your views here.

class CouponListAPI(generics.ListCreateAPIView):
    # queryset = Coupon.objects.all()

    def get_queryset(self):
        # params = self.request.query_params
        # # breakpoint()
        # user_id = self.request.query_params.get('user_id')
        promo_code = self.request.query_params.get("promo_code")
        if promo_code:
            if Coupon.objects.filter(code=promo_code).exists():
                queryset = Coupon.objects.filter(code=promo_code)
            else:
                content = {'errors': 'coupon code not exist'}
                raise ValidationError(content)
        else:
            queryset = Coupon.objects.all()
        return queryset

    # def get_queryset(self):

    serializer_class = CouponSerializer


# class RestaurantDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Restaurant.objects.all()
#     serializer_class = RestaurantSerializer


def index(request):
    return HttpResponse('Hello from Promocode Index page!')


# views.py - Example only
# /use-coupon/?coupon_code=COUPONTEST01

from django.contrib.auth.models import User
# from django.http import HttpResponse
#
from promocode.validations import validate_coupon
# from promocode.models import Co/upon
#
#
# class UseCouponView(restframework_views):
# class UseCouponView(generics.ListCreateAPIView):
class UseCouponView(APIView):

    serializer_class = CouponSerializer

    def get(self, request, *args, **kwargs):
        coupon_code = request.GET.get("promo_code")
        user_id = request.GET.get("user_id")
        try:
            # user_id = int(request.POST['id'])
            user = User.objects.get(id=user_id)
        except  User.DoesNotExist:
            content = {'errors': 'user id not exist'}
            raise ValidationError(content)
            # raise ValidationError(status)
        # user = User.objects.get(username=request.user.username)
        # user = User.objects.get(id=user_code)
        # user = User.objects.first()

        status = validate_coupon(coupon_code=coupon_code, user=user)
        if status['valid']:
            coupon = Coupon.objects.get(code=coupon_code)
            coupon.use_coupon(user=user)
            # return HttpResponse("OK")
            # return Response({'some': 'data'})
            return Response(status)
        raise ValidationError(status)
        return HttpResponse(status['message'])

# class MyOwnView(APIView):
#     def get(self, request):
#         return Response({'some': 'data'})