from rest_framework import generics

from . import models
from . import serializers
# from django.contrib.auth.models import User

from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from sales.models import Order
from sales.serializers import OrderSerializer


class UserListView(generics.ListAPIView):
    # queryset = models.CustomUser.objects.all()
    queryset = User.objects.all().order_by('-id')
    # queryset = queryset.order_by('-id')
    serializer_class = serializers.UserSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

class UserOrdersAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer



@api_view(['POST'])
def customer_login(request):
    """
    Try to login a customer (food orderer)
    """
    data = request.data

    try:
        username = data['username']
        password = data['password']
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    try:
        user = User.objects.get(username=username, password=password)
    except:
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    try:
        user_token = user.auth_token.key
    except:
        user_token = Token.objects.create(user=user)

    data = {'token': user_token}
    return Response(data=data, status=status.HTTP_200_OK)




class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        user = User.objects.get(id=token.user_id)
        return Response({'token': token.key, 'id': token.user_id, 'user_details': user})

