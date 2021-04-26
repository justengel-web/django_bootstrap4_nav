from .settings import mysettings


__all__ = ['get_context']


def get_context(request=None, site_name=None, title=None, hide_container=None, show_sidenav=None, fixed_sidenav=None,
                **kwargs):
    """Context processor to add nav context to every view.

    Args:
        request (HttpRequest): http request.

        site_name (str)[None]: Name of the site to display in the navbar.
        title (str)[None]: Title to display in the browser tab.
    """
    if site_name is None:
        site_name = mysettings.BOOTSTRAP4_SITE_NAME
    if title is None:
        title = mysettings.BOOTSTRAP4_TITLE

    if hide_container is None:
        hide_container = mysettings.BOOTSTRAP4_HIDE_CONTAINER
    if show_sidenav is None:
        show_sidenav = mysettings.BOOTSTRAP4_SHOW_SIDENAV
    if fixed_sidenav is None:
        fixed_sidenav = mysettings.BOOTSTRAP4_FIXED_SIDENAV

    context = kwargs.copy()
    context['DJANGO_BASE_TEMPLATE'] = 'bootstrap4_nav/base.html'

    context['BOOTSTRAP4_SITE_NAME'] = site_name
    context['BOOTSTRAP4_TITLE'] = title

    context['HIDE_CONTAINER'] = hide_container
    context['SHOW_SIDENAV'] = show_sidenav
    context['FIXED_SIDENAV'] = fixed_sidenav

    return context
