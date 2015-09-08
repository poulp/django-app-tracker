from django.conf import settings


def tracker_settings(request):

    return {
        'LOGIN_URL': settings.APPTRACKER['LOGIN_URL'],
        'LOGOUT_URL': settings.APPTRACKER['LOGOUT_URL'],
    }