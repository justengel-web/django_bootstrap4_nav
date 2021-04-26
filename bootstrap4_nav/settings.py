from django.conf import settings

from .utils import static


__all__ = ['mysettings']


class Defaults(object):
    pass


class AppSettings(object):
    def __init__(self, defaults=None):
        super().__init__()

        if defaults is None:
            defaults = Defaults()
        self.defaults = defaults

    def __getattr__(self, name):
        default = getattr(self.defaults, name, None)
        return getattr(settings, name, default)

    def __setattr__(self, name, value):
        if name != 'defaults':
            setattr(self.defaults, name, value)
        else:
            super().__setattr__(name, value)

    def __dir__(self):
        return dir(self.defaults)


DEFAULTS = Defaults()
mysettings = AppSettings(DEFAULTS)


# ========== Defaults ==========
DEFAULTS.BOOTSTRAP4_ICONS_URL = {
    'href': 'https://cdn.jsdelivr.net/npm/bootstrap-icons@1.4.1/font/bootstrap-icons.css'
    }

DEFAULTS.BOOTSTRAP4_NAV_CSS_URL = {
    'href': static('bootstrap4_nav/bootstrap4_nav.css'),
    }

DEFAULTS.BOOTSTRAP4_NAV_JS_URL = {
    'src': static('bootstrap4_nav/bootstrap4_nav.js'),
    }

# ========== Styling ==========
DEFAULTS.BOOTSTRAP4_SITE_NAME = None
DEFAULTS.BOOTSTRAP4_TITLE = None

DEFAULTS.BOOTSTRAP4_HIDE_CONTAINER = False
DEFAULTS.BOOTSTRAP4_SHOW_SIDENAV = False
DEFAULTS.BOOTSTRAP4_FIXED_SIDENAV = False

# ========== User ==========
# DEFAULTS.USER_THUMBNAIL_PROPERTY = ''
# DEFAULTS.USER_BACKGROUND_PROPERTY = ''
# DEFAULTS.USER_THUMBNAIL = 'accounts/default_user.png'
# DEFAULTS.USER_BACKGROUND_IMAGE = 'accounts/default_background.png'
