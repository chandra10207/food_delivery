from django import forms
from food_delivery.models import UserProfileInfo
from django.contrib.auth.models import User
from restaurant.models import Restaurant
from Location.models import Address


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password=forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password',)
        # help_texts = {
        #     'email': 'ERequired Field.',
        # }

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )


class UserProfileInfoForm(forms.ModelForm):
     class Meta():
         model = UserProfileInfo
         fields = ('profile_pic',)


class RestaurantAddressForm(forms.ModelForm):
     class Meta():
         model = Address
         fields = ['unit', 'street_number', 'street_name','suburb','state','post_code']

class RestaurantForm(forms.ModelForm):
    class Meta():
        model = Restaurant
        fields = ("name", "content", "restaurant_banner_image", "restaurant_logo")