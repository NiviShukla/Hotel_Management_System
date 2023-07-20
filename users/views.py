# from django.shortcuts import redirect, render
# from django.contrib.auth.forms import AuthenticationForm


# def login_view(request):
#     login_form = AuthenticationForm()
#     return render(request, 'views/login.html', {'login_form' : login_form})

from django.shortcuts import redirect, render
from django.shortcuts import render
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views import View
from .forms import UserForm
from django.contrib.auth.models import User

from hotel.models import Room, Booking
from .forms import ProfileForm
from .models import Profile


def login_view(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request=request, data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(
                    request, f'You are now logged in as {username}.')
                return redirect('hotel:BookingView')
            else:
                messages.error(request, f'An error occured trying to login.')
        else:
            messages.error(request, f'An error occured trying to login.')
    elif request.method == 'GET':
        login_form = AuthenticationForm()
    return render(request, 'views/login.html', {'login_form': login_form})


@login_required
def logout_view(request):
    logout(request)
    return redirect('main')


class RegisterView(View):

    def get(self, request):
        register_form = UserCreationForm()
        return render(request, 'views/register.html', {'register_form': register_form})

    def post(self, request):
        register_form = UserCreationForm(request.POST)
        if register_form.is_valid():
            user = register_form.save()
            user.refresh_from_db()
            login(request, user)
            messages.success(request, f'Registered successfully. Welcome, {user.username}!')
            return redirect('hotel:BookingView')
        else:
            messages.error(request, f'An error occured trying to register.')
            return render(request, 'views/register.html', {'register_form': register_form})


@method_decorator(login_required, name='dispatch')
class ProfileView(View):

    def get(self, request):
        user_bookings = Booking.objects.filter(user=request.user)
        profile = request.user.profile
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=profile)
        return render(request, 'views/profile.html', {'user_form': user_form,
                                                      'profile_form': profile_form,
                                                      'user_bookings': user_bookings, })

    def post(self, request):
        user_bookings = Booking.objects.filter(user=request.user)
        profile = request.user.profile
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=profile)
        
        if user_form.is_valid() and profile_form.is_valid() :
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')
        else:
            messages.error(request, 'Error updating profile!')
            
        return render(request, 'views/profile.html', {
            'user_form': user_form,
            'profile_form': profile_form,
            'user_bookings': user_bookings,
        })
        
