======================
Django Bootstrap4 Nav
======================
This library was created to make django work with some generic bootstrap4 templates. This library uses the basic
functionality from django-bootstrap4. I use it to match templates with my ``django_materialize_nav`` library.


Setup
=====
Install the library.

.. code-block:: python

    # project/settings.py

    INSTALLED_APPS = [
        "bootstrap4_nav",
        ...
    ]


Setup Context Processors
------------------------
Bootstrap4_nav comes with a context processor to use some settings to change the default base styling.

.. code-block:: python

    # Context Processor to work with settings
    TEMPLATES = [
        {
            ...
            'OPTIONS': {
                'context_processors': [
                    ...
                    'bootstrap4_nav.context_processors.get_context',
                ],
            },
        },
    ]


Alternative way to get the standard context for views

.. code-block:: python

    # views.py

    from bootstrap4_nav.context_processors import get_context


    def show_page(request):
        # Get the context with the style settings
        context = get_context(site_name='demo', title='Basic Content')

        context["object"] = "MyObject"
        return render(request, "my_page.html", context)


Style
=====
The base template can be used by extending the materialize base nav.

.. code-block:: html

    {% extends "bootstrap4_nav/base.html" %}


    {% block nav_items %}
        <li class="navbar-item{% if title == 'Page1' %} active{% endif %}"><a class="nav-link" href="/">Page1</a></li>
        <li class="navbar-item{% if title == 'Page2' %} active{% endif %}"><a class="nav-link" href="/">Page2</a></li>
        <li class="navbar-item{% if title == 'Page3' %} active{% endif %}"><a class="nav-link" href="/">Page3</a></li>
    {% endblock %}

    {% block contents %}
    <div>
        <p>My Content goes here</p>
    </div>
    {% endblock %}


Styling controls
----------------

Bootstrap4_nav comes with several style options used in the template context variables listed below.

  * BOOTSTRAP4_SITE_NAME
  * BOOTSTRAP4_TITLE

If you went through the ``Setup Context Processors`` step then you can modify several settings to change the default style.
This is an alternative to manually providing all of the template context variables.


.. code-block:: python

    # settings.py

    BOOTSTRAP4_SITE_NAME = None  # Display this name in the navbar as the main name
    BOOTSTRAP4_TITLE = None  # This is the page title displayed as the browser tab name
