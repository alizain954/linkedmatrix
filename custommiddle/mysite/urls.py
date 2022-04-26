
from django.urls import path
from . import views
urlpatterns = [
    path('signup', views.Sign_up, name='signup'),
    path('login', views.User_login, name='login'),
    path('logout', views.Logout, name='logout'),
    path('home', views.home, name='home')
]