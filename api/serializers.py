from rest_framework import serializers
from . import models
from django.contrib.auth.models import User

# from rest_auth.registration import serializers
from allauth.account import app_settings as allauth_settings
from allauth.utils import email_address_exists
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email

from django.contrib.auth.models import Group

from rest_auth.models import TokenModel
from rest_framework.authtoken.models import Token

from allauth.utils import (email_address_exists,
                           get_username_max_length)
import rest_auth.serializers
from sales.models import Order
from sales.models import OrderItem

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        # model = models.CustomUser
        model = User
        fields = ('id', 'email', 'username', 'first_name', 'last_name')



# class CustomRestRegisterSerializer(serializers.ModelSerializer):
#     class Meta:
#         # model = models.CustomUser
#         model = User
#         fields = ('id', 'email', 'username', 'first_name', 'last_name', 'password')



class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(
        max_length=get_username_max_length(),
        min_length=allauth_settings.USERNAME_MIN_LENGTH,
        required=allauth_settings.USERNAME_REQUIRED
    )
    # email = serializers.EmailField(required=allauth_settings.EMAIL_REQUIRED)
    email = serializers.EmailField(required=True)
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    password = serializers.CharField(required=True, write_only=True)
    # password2 = serializers.CharField(required=True, write_only=True)

    def validate_username(self, username):
        username = get_adapter().clean_username(username)
        return username

    def validate_email(self, email):
        email = get_adapter().clean_email(email)
        if allauth_settings.UNIQUE_EMAIL:
            if email and email_address_exists(email):
                # raise serializers.ValidationError( _("A user is already registered with this e-mail address."))
                raise serializers.ValidationError("A user is already registered with this e-mail address.")
        return email

    def validate_password(self, password):
        return get_adapter().clean_password(password)

    # def validate(self, data):
    #     if data['password1'] != data['password2']:
    #         # raise serializers.ValidationError(_("The two password fields didn't match."))
    #         raise serializers.ValidationError("The two password fields didn't match.")
    #     return data

    # def custom_signup(self, request, user):
    #     user.first_name = self.validated_data.get('first_name', '')
    #     user.last_name = self.validated_data.get('last_name', '')
    #     user.password = self.validated_data.get('password', '')
    #     user.save(update_fields=['first_name', 'last_name','password'])

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
            'password1': self.validated_data.get('password', ''),
            'email': self.validated_data.get('email', ''),
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        setup_user_email(request, user, [])
        # user.profile.save()
        group = Group.objects.get(name='Customer')
        user.groups.add(group)
        user.save()
        return user


class CustomTokenSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)
    class Meta:
        model = TokenModel
        fields = ('key', 'user',)


class LoginSerializer(rest_auth.serializers.LoginSerializer):

    def get_fields(self):
        fields = super(LoginSerializer, self).get_fields()
        # breakpoint()
        fields['email'] = fields['username']

        # breakpoint()
        del fields['username']
        return fields

    def validate(self, attrs):
        usernameoremail = attrs['email']
        if User.objects.filter(email=usernameoremail).exists():
            # new_user = User(email=usernameoremail)
            new_user = User.objects.get(email=usernameoremail)
            username = new_user.username
            # breakpoint()
            attrs['username'] = username
            del attrs['email']
            return super(LoginSerializer, self).validate(attrs)
        else:
            if User.objects.filter(username=usernameoremail).exists():
                # new_user = User(email=usernameoremail)
                # username = new_user.username
                attrs['username'] = attrs['email']
                del attrs['email']
                # breakpoint()
                return super(LoginSerializer, self).validate(attrs)
            else:
                raise serializers.ValidationError("username or email not valid")
        return super(LoginSerializer, self).validate(attrs)

