from django.conf.urls import patterns, url
from django.contrib.auth import views as auth_views

from . import base
from . import utils


class AuthenticateViews(base.Views):
    """login and logout views
    """
    login_url_pattern = r'^login/$'
    logout_url_pattern = r'^logout/$'
    login_view = utils.to_method(
        auth_views.login, template_name='auth/login.html')
    logout_view = utils.to_method(
        auth_views.logout, template_name='auth/logout.html')

    def __init__(self, name=None, app_name=None):
        super(AuthenticateViews, self).__init__(
            name or 'auth', app_name or 'auth')

    def login(self, request, *args, **kwargs):
        return self.login_view(request, *args, **kwargs)

    def logout(self, request, *args, **kwargs):
        return self.logout_view(request, *args, **kwargs)

    def get_urls(self):
        urlpatterns = patterns(
            '',
            url(self.login_url_pattern,
                self.wrap_view(self.login), name='login'),
            url(self.logout_url_pattern,
                self.wrap_view(self.logout), name='logout'),
        )
        return urlpatterns

authenticate_views = AuthenticateViews()
