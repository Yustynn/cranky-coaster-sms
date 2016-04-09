from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^send/', include('send.urls')),
    url(r'^admin/', admin.site.urls),
]
