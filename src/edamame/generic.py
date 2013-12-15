from django.conf.urls import patterns, url
from django.views import generic

from . import base


class BaseModelViews(base.Views):
    model = None
    success_url = None
    list_view = None
    create_view = None
    detail_view = None
    update_view = None
    delete_view = None
    index_url_pattern = r'^$'
    add_url_pattern = r'^add/$'
    show_url_pattern = r'^(?P<pk>\d+)/$'
    edit_url_pattern = r'^(?P<pk>\d+)/edit/$'
    delete_url_pattern = r'^(?P<pk>\d+)/delete/$'
    initkwargs = {}

    def __init__(self, name=None, app_name=None):
        """If name is empty, use the name of lowercase of model class.
        """
        if self.model:
            model_name = self.model.__name__.lower()
        else:
            model_name = None
        super(BaseModelViews, self).__init__(
            name or model_name, app_name or model_name)

    def _as_view(self, view_or_class, initkwargs_base=None):
        """If view_or_class is Django generic View, return object by as_view.
        """
        if issubclass(view_or_class, generic.View):
            # common initkwargs
            initkwargs = initkwargs_base or {}
            initkwargs.update({'model': self.model})
            initkwargs.update(self.initkwargs)
            return view_or_class.as_view(**initkwargs)
        return view_or_class

    def index(self, request, *args, **kwargs):
        """ListView
        """
        view = self._as_view(self.list_view)
        return view(request, *args, **kwargs)

    def add(self, request, *args, **kwargs):
        """CreateView
        """
        initkwargs = {}
        if self.success_url:
            initkwargs = {'success_url': self.success_url}
        view = self._as_view(self.create_view, initkwargs)
        return view(request, *args, **kwargs)

    def show(self, request, *args, **kwargs):
        """DetailView
        """
        initkwargs = {}
        view = self._as_view(self.detail_view, initkwargs)
        return view(request, *args, **kwargs)

    def edit(self, request, *args, **kwargs):
        """UpdateView
        """
        initkwargs = {}
        if self.success_url:
            initkwargs = {'success_url': self.success_url}
        view = self._as_view(self.update_view, initkwargs)
        return view(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """DeleteView
        """
        initkwargs = {}
        if self.success_url:
            initkwargs = {'success_url': self.success_url}
        view = self._as_view(self.delete_view, initkwargs)
        return view(request, *args, **kwargs)

    def get_urls(self):
        urlpatterns = []
        if self.list_view:
            urlpatterns += patterns(
                '',
                url(self.index_url_pattern,
                    self.wrap_view(self.index), name='index'))
        if self.create_view:
            urlpatterns += patterns(
                '',
                url(self.add_url_pattern,
                    self.wrap_view(self.add), name='add'))
        if self.detail_view:
            urlpatterns += patterns(
                '',
                url(self.show_url_pattern,
                    self.wrap_view(self.show), name='show'))
        if self.detail_view:
            urlpatterns += patterns(
                '',
                url(self.edit_url_pattern,
                    self.wrap_view(self.edit), name='edit'))
        if self.delete_view:
            urlpatterns += patterns(
                '',
                url(self.delete_url_pattern,
                    self.wrap_view(self.delete), name='delete'))
        return urlpatterns


class ModelViews(BaseModelViews):
    list_view = generic.ListView
    create_view = generic.CreateView
    detail_view = generic.DetailView
    update_view = generic.UpdateView
    delete_view = generic.DeleteView
