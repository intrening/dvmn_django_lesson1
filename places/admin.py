from django.contrib import admin
from django.utils.html import format_html
from adminsortable2.admin import SortableInlineAdminMixin

from .models import Place, Image


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    fields = ('image', 'get_preview', 'my_order')
    readonly_fields = ['get_preview',]

    def get_preview(self, obj):
        return format_html(
            '<img src="{}" height=200px" />',
            obj.image.url,
        )


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]
    
