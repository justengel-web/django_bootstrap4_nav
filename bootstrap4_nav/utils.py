from django.forms.utils import flatatt
from django.utils.html import format_html
from django.utils.safestring import mark_safe


def render_tag(tag, inner_html=None, end_tag=True, **attrs):
    if inner_html is None:
        inner_html = ''

    ending = ''
    if end_tag:
        ending = '</{tag}>'

    fmt = '<{tag} {attrs}>{inner_html}' + ending
    return format_html(fmt, tag=tag, attrs=mark_safe(flatatt(attrs)), inner_html=str(inner_html))
