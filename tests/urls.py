from django.conf.urls import include, url
from django.contrib import admin
from openwisp_network_topology import urls as urls


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(urls)),
]
