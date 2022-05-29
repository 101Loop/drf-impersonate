=====
Usage
=====

To use drf impersonate in a project, add it to your `INSTALLED_APPS`:

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
