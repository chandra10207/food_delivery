from django.shortcuts import render
from food_delivery.forms import UserForm, UserProfileInfoForm, RestaurantForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import Group

def index(request):
    return render(request, 'food_delivery/index.html')


@login_required
def special(request):
    return HttpResponse("You are logged in !")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        restaurant_form = RestaurantForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid() and restaurant_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.is_staff = True
            group = Group.objects.get(name='Restaurant')
            user.groups.add(group)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                print('found it')
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
            restaurant = restaurant_form.save(commit=False)
            restaurant.owner = user

            if 'restaurant_banner_image' in request.FILES:
                print('banner image found it')
                restaurant.restaurant_banner_image = request.FILES['restaurant_banner_image']

            if 'restaurant_logo' in request.FILES:
                print('logo image found it')
                restaurant.restaurant_logo = request.FILES['restaurant_logo']

            restaurant.save()

        else:
            print(user_form.errors, profile_form.errors, restaurant_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
        restaurant_form = RestaurantForm()
    return render(request, 'food_delivery/register.html',
                  {'user_form': user_form,
                   'restaurant_form': restaurant_form,
                   'profile_form': profile_form,
                   'registered': registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username, password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'food_delivery/login.html', {})
