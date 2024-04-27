# src/app/shop/apps.py

# Django modul
from django.apps import AppConfig


class ShopConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    # name = "shop"
    name = "app.shop"
