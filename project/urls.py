from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^', include('project.apps.pages.urls')),
    url(r'^account/', include('project.apps.account.urls')),
    url(r'^auth/', include('project.apps.auth.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('project.apps.api.base.urls'), name='api'),
    url(r'^', include('project.apps.cms.urls'), name='cms'),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
