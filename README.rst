=============================
drf impersonate
=============================

.. image:: https://badge.fury.io/py/drf-impersonate.svg
    :target: https://badge.fury.io/py/drf-impersonate

.. image:: https://github.com/101loop/drf-impersonate/workflows/CI/badge.svg
    :target: https://github.com/101loop/drf-impersonate

.. image:: https://codecov.io/gh/101loop/drf-impersonate/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/101loop/drf-impersonate

.. image:: https://results.pre-commit.ci/badge/github/101Loop/drf-impersonate/master.svg
    :target: https://results.pre-commit.ci/latest/github/101Loop/drf-impersonate/master
    :alt: pre-commit.ci status

Documentation
-------------

The full documentation is at https://drf-impersonate.readthedocs.io.

Quickstart
----------

Install drf impersonate::

    pip install drf-impersonate

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'drf_impersonate.apps.DrfImpersonateConfig',
        ...
    )

Add drf impersonate's URL patterns:

.. code-block:: python

    from drf_impersonate import urls as drf_impersonate_urls


    urlpatterns = [
        ...
        url(r'^', include(drf_impersonate_urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox


Development commands
---------------------

::

    pip install -r requirements_dev.txt
    invoke -l


Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
