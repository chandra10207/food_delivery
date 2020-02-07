from rest_framework import serializers
from food_delivery.models import UserProfileInfo
from Location.serializers import AddressSerializer
from Location.models import Address

class ProfileSerializer(serializers.ModelSerializer):

    address = AddressSerializer()

    class Meta:
        model = UserProfileInfo
        # fields = "__all__"
        fields = ['id', 'user', 'phone', 'balance', 'address']

    # def create(self, validated_data):
    #     addressess_data = validated_data.pop('address')
    #     musician = Address.objects.create(**validated_data)
    #     for address_data in addressess_data:
    #         Album.objects.create(artist=musician, **album_data)
    #     return musician

    def update(self, instance, validated_data):

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

        address = validated_data.pop('address')
        # addresses = instance.address
        addresses = Address.objects.create(created_by=instance.user)
        # breakpoint()
        # address_list = list(addresses)
        user = validated_data.get('user')

        instance.phone = validated_data.get('phone', instance.phone)

        # for ad_data in addresses_data:
        unit = address.get('unit')
        # breakpoint()
        addresses.unit = unit
        # breakpoint()
        addresses.street_number = address.get('street_number')
        addresses.street_name = address.get('street_name')
        addresses.suburb = address.get('suburb')
        addresses.state = address.get('state')
        addresses.post_code = address.get('post_code')
        # addresses.created_by = user
        addresses.save()
        instance.address = addresses
        instance.save()
        return instance
