from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from users.views import sign_in, sign_up, profile_change, profile, logout


app_name = 'users'

urlpatterns = [
    path('sign-in', sign_in, name='sign-in'),
    path('sign-up', sign_up, name='sign-up'),
    path('profile_change', profile_change, name='profile_change'),
    path('profile', profile, name='profile'),
    path('logout', logout, name='logout')
]