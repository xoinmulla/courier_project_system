# home/urls.py
from django.urls import path
from .views import home_view, about_view, contact_view
from django.contrib.auth.views import LogoutView

app_name = 'home'

urlpatterns = [
    path('', home_view, name='home'),
    path('about/', about_view, name='about'),
    path('contact/', contact_view, name='contact'),
    path('logout/', LogoutView.as_view(), name='logout'),  
]
