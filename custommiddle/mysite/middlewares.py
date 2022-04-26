import logging
import time

logger = logging.getLogger(__name__)
from django.utils.timezone import now
from django.conf import settings
from django.core.cache import cache
from django.utils import timezone
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from django.core.cache import cache
import datetime
from django.contrib.auth.models import User
from django.core.cache import cache
from django.utils import timezone
# other user model import
CACHE_TTL = getattr(settings ,'CACHE_TTL' , DEFAULT_TIMEOUT)

global ip
ip = 0
login_time = (datetime.datetime.now())
def FilterIPMiddleware(get_response):
    def my_ip(request):
        ip = request.META.get('REMOTE_ADDR')
        logger.warning('User come this  ' + ip + 'on page' )
        print(ip)
        response = get_response(request)
        logger.warning('Homepage was accessed at ' + str(login_time) + ' hours! with that  ')
        ipcome = cache.get(ip)
        iplast = cache.set(ipcome)
        a = time.sleep(60)
        if iplast in a >=5:
            return ('User is Temporirly block')

        return response
    return my_ip



def last_visit_middleware(get_response):

    def middleware(request):
        """
        Save the time of last user visit
        """
        response = get_response(request)

        if request.session.session_key:
            key = "recently-seen-{}".format(request.session.session_key)
            recently_seen = cache.get(key)
            print(recently_seen )

            # is_authenticated hits db as it selects user row
            # so we will hit it only if user is not recently seen
            if not recently_seen and request.user.is_authenticated:
                User.objects.filter(id=request.user.id) \
                    .update(last_visit=(datetime.datetime.now()))
                visit_time = 60 * 30    # 30 minutes
                cache.set(key, 1, visit_time)


        return response

    return middleware

