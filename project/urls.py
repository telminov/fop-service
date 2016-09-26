from django.conf.urls import url, include
import core.urls

urlpatterns = [
    url(r'^', include(core.urls)),
]
