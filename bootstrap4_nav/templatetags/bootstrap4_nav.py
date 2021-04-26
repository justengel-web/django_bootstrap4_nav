from bootstrap4.templatetags.bootstrap4 import *
from bootstrap4_nav.utils import render_tag
from bootstrap4_nav.settings import mysettings


@register.simple_tag
def bootstrap4_icons_url():
    return render_tag('link', end_tag=False, rel='stylesheet', **mysettings.BOOTSTRAP4_ICONS_URL)


@register.simple_tag
def bootstrap4_nav_css_url():
    return render_tag('link', end_tag=False, rel='stylesheet', **mysettings.BOOTSTRAP4_NAV_CSS_URL)


@register.simple_tag
def bootstrap4_nav_js_url():
    return render_tag('script', type='text/javascript', **mysettings.BOOTSTRAP4_NAV_JS_URL)
