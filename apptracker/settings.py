
from django.conf import settings

USER_SETTINGS = getattr(settings, 'APPTRACKER', None)

DEFAULTS = {
    'LOGIN_URL' : '/login',
    'LOGOUT_URL': '/logout'
}


class TrackerSettings(object):
    def __init__(self, user_settings=None, defaults=None):
        self.user_settings = user_settings or {}
        self.defaults = defaults or DEFAULTS

    def __getattr__(self, attr):
        if attr not in self.defaults.keys():
            raise AttributeError("Invalid API setting: '%s'" % attr)
        try:
            # Check if present in user settings
            val = self.user_settings[attr]
        except KeyError:
            # Fall back to defaults
            val = self.defaults[attr]

        # Cache the result
        setattr(self, attr, val)
        return val

tracker_settings = TrackerSettings(USER_SETTINGS, DEFAULTS)