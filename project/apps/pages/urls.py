from django.conf.urls import include, url

from . import views as main_views

urlpatterns = [
    url(r'^$', main_views.index, name='index'),
    url(r'^contact/$', main_views.contact, name='contact'),
    url(r'^captcha/', include('captcha.urls')),
]
