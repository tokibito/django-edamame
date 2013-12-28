from django.shortcuts import render
from django.conf.urls import patterns, url
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

from edamame import base, utils, generic

from . import models


class SiteViews(base.Views):
    def index(self, request):
        """view function
        """
        return render(request, 'index.html')

    test_page = utils.to_method(
        TemplateView.as_view(template_name='test_page.html'))

    def get_urls(self):
        urlpatterns = patterns(
            '',
            url(r'^$', self.wrap_view(self.index), name='index'),
            url(r'^test_page$',
                self.wrap_view(self.test_page), name='test_page'),
        )
        return urlpatterns

site_views = SiteViews()


class NoteViews(generic.ModelViews):
    model = models.Note
    success_url = reverse_lazy('note:index')

note_views = NoteViews()


class MembersOnlyViews(base.Views):
    members_only = utils.to_method(render, template_name='members_only.html')
    view_decorators = (
        (login_required, (), {'login_url': 'auth:login'}),
    )

    def get_urls(self):
        urlpatterns = patterns(
            '',
            url(r'^$', self.wrap_view(self.members_only), name='members_only'),
        )
        return urlpatterns

members_only_views = MembersOnlyViews()
