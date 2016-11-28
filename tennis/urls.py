from django.conf.urls import url, include

from tennis import api


urlpatterns = [
    url(r'^', include(api.router.urls)),
]
