from django.conf import settings
from django.contrib.staticfiles.templatetags.staticfiles import static

__all__ = ['mysettings']


class Defaults(object):
    pass


class AppSettings(object):
    def __init__(self, defaults=None):
        self.defaults = defaults

    def __getattr__(self, name):
        default = getattr(self.defaults, name, None)
        return getattr(settings, name, default)

    def __dir__(self):
        return dir(self.defaults)


DEFAULTS = Defaults()
mysettings = AppSettings(DEFAULTS)


# ========== Defaults ==========
DEFAULTS.BOOTSTRAP4_NAV_CSS_URL = {
    'href': static('bootstrap4_nav/bootstrap4_nav.css'),
    }

DEFAULTS.BOOTSTRAP4_NAV_JS_URL = {
    'src': static('bootstrap4_nav/bootstrap4_nav.js'),
    }

# ========== Styling ==========
DEFAULTS.BOOTSTRAP4_SITE_NAME = None
DEFAULTS.BOOTSTRAP4_TITLE = None

# ========== User ==========
# DEFAULTS.USER_THUMBNAIL_PROPERTY = ''
# DEFAULTS.USER_BACKGROUND_PROPERTY = ''
# DEFAULTS.USER_THUMBNAIL = 'accounts/default_user.png'
# DEFAULTS.USER_BACKGROUND_IMAGE = 'accounts/default_background.png'
