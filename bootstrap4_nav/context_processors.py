from .settings import mysettings


__all__ = ['get_context']


def get_context(request=None, site_name=None, title=None):
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

    return {
        'BOOTSTRAP4_SITE_NAME': site_name,
        'BOOTSTRAP4_TITLE': title,
        }
