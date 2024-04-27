# src/config/urls.py

# Django modules
from django.contrib import admin
from django.urls import path

# Locals
from app.shop.views import hello_world_view

urlpatterns = [
    path("admin/", admin.site.urls),
    # app/shop/views
    path("hello/", hello_world_view),
]
