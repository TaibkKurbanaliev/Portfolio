from django.urls import path

from users.views import sign_in, sign_up, profile_change

app_name = 'users'

urlpatterns = [
    path('sign-in', sign_in, name='sign-in'),
    path('sign-up', sign_up, name='sign-up'),
    path('profile_change', profile_change, name='profile_change'),
]