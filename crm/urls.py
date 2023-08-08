from django.contrib import admin
from django.urls import path, include
from django.urls import re_path


# Django admin URLS
urlpatterns = [
    re_path("^admin/", admin.site.urls),
]

# Including the urls from all the applications
API_PATH = "api/v1"
urlpatterns += [
    path(API_PATH + "/", include("api.urls")),  # api
]
