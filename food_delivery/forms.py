from django import forms
from food_delivery.models import UserProfileInfo
from django.contrib.auth.models import User
from restaurant.models import Restaurant


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('first_name', 'last_name', 'username','password','email')


class UserProfileInfoForm(forms.ModelForm):
     class Meta():
         model = UserProfileInfo
         fields = ('portfolio_site', 'profile_pic')


class RestaurantForm(forms.ModelForm):
    class Meta():
        model = Restaurant
        fields = ("name", "content", "banner_image", "logo")