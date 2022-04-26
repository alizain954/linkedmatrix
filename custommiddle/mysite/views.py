from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login , logout
from . serializers import *
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import SessionAuthentication
from django.contrib.auth.models import User
from .models import *
from . middlewares import *
import datetime
import logging
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle

from . throttling import *


CACHE_TTL = getattr(settings ,'CACHE_TTL' , DEFAULT_TIMEOUT)
# Get an instance of a logger
logger = logging.getLogger(__name__)
# Create your views here.
login_time = (datetime.datetime.now())
logout_time = 'out'
# ip = 1

class StudentQuery(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    throttle_classes = [AnonRateThrottle, Goldthrottlin, Silverthrottlin, Bronzethrottlin]


def Sign_up(request):
    if request.method == 'POST':
        f = request.POST[ 'fname' ]
        l = request.POST[ 'lname' ]
        e = request.POST[ 'email' ]
        con = request.POST[ 'contact' ]
        gen = request.POST[ 'gender' ]
        p = request.POST[ 'pwd' ]
        company = request.POST[ 'company' ]
        try:
            user = User.objects.create_user(first_name=f, last_name=l, username=e, password=p)
            User_signup.objects.create(user=user, mobile=con, gender=gen,  company=company)
            return redirect('login')
        except:
            return HttpResponse('is show error usernot save')
    return render(request, 'Sign_up.html')

# Login page
def User_login(request):
    if request.method == 'POST':
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        if user is not None:
            login(request, user)
            # ip = request.META.get('REMOTE_ADDR')
            # ip = FilterIPMiddleware()
            logger.warning(login_time )

            # print(str(datetime.datetime.now()))
            return redirect('home')
    return render(request, 'log_in.html')

def Logout(request):
    # ip = request.META.get('REMOTE_ADDR')
    logout_time = (datetime.datetime.now())
    loging_total = logout_time - login_time
    logger.warning('Logout this ip ' + str(loging_total) + ' hours! with that  ')
    print(loging_total)
    # logger.warning('total time of this ip' + ip + 'remain login is' + time_calculate())
    logout(request)
    return redirect('login')

# def time_calculate():
#     time_1 = datetime.timedelta(login_time)
#     time_2 = datetime.timedelta(logout_time)
#
#     time_interval = (time_2) - (time_1)
#     print(time_interval)
#
#
#     return redirect('login')

def home(request):
    return render(request, 'home.html')