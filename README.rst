==============
Django Edamame
==============

One idea of Class-based view module.

.. image:: https://travis-ci.org/tokibito/django-edamame.png
   :target: https://travis-ci.org/tokibito/django-edamame

Django Edamame gives you inheritable module to bundle the multiple view functions like django.contrib.admin application.

Edamame corresponds to the following problems:

* Reuse URL pattern.
* Creating an application with a similar view function set.

Author
======

* Shinya Okano

Simple example
==============

Inherits the ``Views`` class, and implement the method of view function. And implement ``get_urls`` method to return the URL pattern.

In order to use a views class, it create an instance in the module.

::

   from edamame import base

   class SiteViews(base.Views):
       def index(self, request):
           """view function
           """
           return render(request, 'index.html')

       def get_urls(self):
           urlpatterns = patterns(
               '',
               url(r'^$', self.wrap_view(self.index), name='index'),
           )
           return urlpatterns

   site_views = SiteViews()

``urls`` property of views instance, it can be passed to ``include`` function in ``urls.py``.

::

   from django.conf.urls import patterns, include, url
   from note.views import site_views

   urlpatterns = patterns('',
       url(r'', include(site_views.urls)),
   )

Generic view example
====================

Import the ``ModelViews`` class, and inherits.

::

   from django.core.urlresolvers import reverse_lazy
   from edamame import generic
   from . import models


   class NoteViews(generic.ModelViews):
       model = models.Note
       success_url = reverse_lazy('note:index')

   note_views = NoteViews()

In ``urls.py``, use the ``include`` function.

::

   from django.conf.urls import patterns, include, url
   from note.views import note_views

   urlpatterns = patterns('',
       url(r'note/', include(note_views.urls)),
   )

Example Project
===============

``example`` directory in the repository is an example project.

If you have installed Django and Edamame, can run immediately.

::

   $ cd example
   $ python manage.py syncdb
   $ python manage.py runserver

License
=======

* MIT License
