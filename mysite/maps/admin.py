from django.contrib import admin

from .models import PolygonPoints


class PolygonLocation(admin.TabularInline):
    model = PolygonPoints


admin.site.register(PolygonPoints)
