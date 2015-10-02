django-app-tracker
=============================

.. image:: http://img.shields.io/travis/poulp/django-app-tracker/master.svg?style=flat-square
    :target: https://travis-ci.org/poulp/django-app-tracker
     
.. image:: http://img.shields.io/requires/github/poulp/django-app-tracker.svg?style=flat-square
    :target: https://requires.io/github/poulp/django-app-tracker/requirements/?branch=master

.. image:: http://img.shields.io/coveralls/poulp/django-app-tracker.svg?style=flat-square
    :target: https://coveralls.io/r/poulp/django-app-tracker?branch=master

------------------------

Issue tracker application for django. Work with python3 and Django 1.8.

Quick start
-----------

1. To install ``django-app-tracker`` simply run::

    python setup.py install

2. Add "apptracker" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'django.contrib.humanize',
        'apptracker',
    )

3. Add "tracker_settings" to your TEMPLATE_CONTEXT_PROCESSORS setting like this::

    TEMPLATE_CONTEXT_PROCESSORS = (
        ...
        'apptracker.context_processors.tracker_settings',
    )

4. Add this lines at the end of your settings::

    APPTRACKER = {
        'LOGIN_URL': '/login',
        'LOGOUT_URL': '/logout',
    }

5. Include the apptracker URLconf in your project urls.py like this::

    url(r'^tracker/', include('apptracker.urls')),

6. Run `python manage.py migrate` to create the apptracker models.

7. Visit http://127.0.0.1:8000/tracker/projects

Screenshots : http://poulp.github.io/apptracker.html
