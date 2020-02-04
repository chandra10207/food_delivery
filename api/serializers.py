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
from store_follower.serializers import StoreFollowerSerializer
from sales.serializers import OrderSerializer
from food_delivery.serializers import ProfileSerializer
from food_delivery.models import UserProfileInfo
from Location.models import Address

from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):

    # profile = ProfileSerializer()

    class Meta:
        # restaurant_
        # model = models.CustomUser
        model = User
        fields = ('id', 'email', 'username', 'first_name', 'last_name','groups', 'profile', 'followed_stores','orders')


class UserDetailSerializer(serializers.ModelSerializer):

    orders = OrderSerializer(many=True, read_only=True)
    followed_stores = StoreFollowerSerializer(many=True, read_only=True)
    profile = ProfileSerializer()

    class Meta:
        # restaurant_
        # model = models.CustomUser
        model = User
        fields = ('id', 'email', 'username', 'first_name', 'last_name', 'groups', 'profile', 'followed_stores','orders')



    def update(self, instance, validated_data):

        user = validated_data.get('id')
        profile_data = validated_data.pop('profile')
        address_data = profile_data.pop('address')
        address_obj = Address.objects.create(created_by=user)
        profile_obj = instance.profile
        # breakpoint()
        # address_list = list(addresses)
        profile_obj.phone = profile_data.get('phone', profile_obj.phone)
        address_obj.unit = address_data.get('unit')
        address_obj.street_number = address_data.get('street_number')
        address_obj.street_name = address_data.get('street_name')
        address_obj.suburb = address_data.get('suburb')
        address_obj.state = address_data.get('state')
        address_obj.post_code = address_data.get('post_code')
        # addresses.created_by = user
        address_obj.save()
        profile_obj.address = address_obj
        profile_obj.save()
        instance.save()
        return instance




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
    is_driver = serializers.NullBooleanField(required=False)
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
        # data = request.DATA
        # breakpoint()
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        setup_user_email(request, user, [])
        # user.profile.save()
        if self.data['is_driver']:
            group = Group.objects.get(name='Delivery Person')
        else:
            group = Group.objects.get(name='Customer')
        user.groups.add(group)
        user.save()
        profile = UserProfileInfo.objects.create(user=user)
        user.profile = profile
        return user

    # def create(self, validated_data):
    #     albums_data = validated_data.pop('album_musician')
    #     musician = Musician.objects.create(**validated_data)
    #     for album_data in albums_data:
    #         Album.objects.create(artist=musician, **album_data)
    #     return musician
    #
    # def update(self, instance, validated_data):
    #     albums_data = validated_data.pop('album_musician')
    #     albums = (instance.album_musician).all()
    #     albums = list(albums)
    #     instance.first_name = validated_data.get('first_name', instance.first_name)
    #     instance.last_name = validated_data.get('last_name', instance.last_name)
    #     instance.instrument = validated_data.get('instrument', instance.instrument)
    #     instance.save()
    #
    #     for album_data in albums_data:
    #         album = albums.pop(0)
    #         album.name = album_data.get('name', album.name)
    #         album.release_date = album_data.get('release_date', album.release_date)
    #         album.num_stars = album_data.get('num_stars', album.num_stars)
    #         album.save()
    #     return instance


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
        # if '@' in username:
        #     kwargs = {'email': username}
        # else:
        #     kwargs = {'mobile_phone': username}
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

