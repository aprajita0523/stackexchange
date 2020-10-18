from django.urls import path 

from .views import my_profile_view


app_name = 'profiles'  #important

urlpatterns = [
    path('myprofile/',my_profile_view, name='my_profile_view'),
]


#http://127.0.0.1:8000/profiles -- will already be defined in main.urls.py