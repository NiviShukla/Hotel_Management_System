from django.urls import path
from django.contrib.auth.views import LogoutView
from users.views import login_view, RegisterView, ProfileView

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(next_page='hotel:main'), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
]
