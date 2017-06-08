from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views as main_views

urlpatterns = [
    url(r'^login/$', auth_views.login,
        {
            'template_name': 'auth/login.html',
            'redirect_authenticated_user': True,
        },
        name='login'),
    url(r'^signup/$', main_views.signup, name='signup'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'home'}, name='logout'),
]
