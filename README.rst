django-app-tracker
=============================

.. image:: http://img.shields.io/travis/poulp/django-app-tracker/master.svg?style=flat-square
    :target: https://travis-ci.org/poulp/django-app-tracker
     
.. image:: http://img.shields.io/requires/github/poulp/django-app-tracker.svg?style=flat-square
    :target: https://requires.io/github/poulp/django-app-tracker/requirements/?branch=master

.. image:: http://img.shields.io/coveralls/poulp/django-app-tracker.svg?style=flat-square
    :target: https://coveralls.io/r/poulp/django-app-tracker?branch=master

------------------------

Issue tracker application for django. Work with python3 and Django 1.7, work in progress.

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

3. Include the apptracker URLconf in your project urls.py like this::

    url(r'^tracker/', include('apptracker.urls')),

4. Run `python manage.py migrate` to create the apptracker models.

5. Visit http://127.0.0.1:8000/tracker/
