from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from edamame.auth import authenticate_views
from note.views import site_views, note_views, members_only_views


urlpatterns = patterns('',
    url(r'', include(site_views.urls)),
    url(r'note/', include(note_views.urls)),
    url(r'auth/', include(authenticate_views.urls)),
    url(r'members_only/', include(members_only_views.urls)),

    url(r'^admin/', include(admin.site.urls)),
)
