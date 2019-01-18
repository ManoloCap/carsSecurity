from django.contrib import admin
from django.conf.urls import url
from .views import login, validate_Token


urlpatterns = [
    url('admin/', admin.site.urls),
    url('api/login', login),
    url('api/validateToken', validate_Token)
]
