from django.shortcuts import render
from rest_framework import generics
from django.http import HttpResponse
from rest_framework.validators import ValidationError
from tax.serializers import TaxSerializer
from tax.models import Tax

# Create your views here.


class TaxListAPI(generics.ListCreateAPIView):

    # def get_queryset(self):
    #     params = self.request.query_params
    #     # breakpoint()
    #     user_id = self.request.query_params.get('user_id')
    #     if user_id:
    #         if User.objects.filter(id=user_id).exists():
    #             queryset = StoreFollower.objects.filter(user_id=user_id)
    #         else:
    #             content = {'errors': 'user id not exist'}
    #             raise ValidationError(content)
    #     else:
    #         queryset = StoreFollower.objects.all()
    #     return queryset
    queryset = Tax.objects.all()
    serializer_class = TaxSerializer
