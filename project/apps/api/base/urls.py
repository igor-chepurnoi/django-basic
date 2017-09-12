from django.conf.urls import url, include
from rest_framework.documentation import include_docs_urls

from project.apps.api.base.router import api_urlpatterns as api_v1

urlpatterns = [
    url(r'^v1/', include(api_v1, namespace='v1')),
    url(r'^docs/', include_docs_urls(title='Basic API')),
    url(r'^auth/', include('rest_framework.urls')),
]
