=============================
django-app-tracker
=============================

.. image:: https://travis-ci.org/poulp/django-app-tracker.svg
    :target: https://travis-ci.org/poulp/django-app-tracker

.. image:: https://requires.io/github/poulp/django-app-tracker/requirements.svg?branch=master
     :target: https://requires.io/github/poulp/django-app-tracker/requirements/?branch=master
     :alt: Requirements Status

.. image:: https://coveralls.io/repos/poulp/django-app-tracker/badge.svg?branch=master
     :target: https://coveralls.io/r/poulp/django-app-tracker?branch=master
     :alt: Coverage

------------------------

Issue tracker application for django. Work with python3 and Django 1.7, work in progress.

Quick start
-----------

1. To install `django-app-tracker` simply run::

    python setup.py install

2. Add "polls" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'apptracker',
    )

3. Include the polls URLconf in your project urls.py like this::

    url(r'^tracker/', include('apptracker.urls')),

4. Run `python manage.py migrate` to create the apptracker models.

5. Visit http://127.0.0.1:8000/tracker/

.. image:: http://zestedesavoir.com/media/galleries/1485/c623e024-650d-41e9-a1d3-de4e04bf91d6.png
     :alt: Issues
