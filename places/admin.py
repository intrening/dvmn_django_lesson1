from django.contrib import admin
from django.utils.html import format_html
from adminsortable2.admin import SortableInlineAdminMixin

from .models import Place, Image


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    fields = ['image', 'get_preview', 'order', ]
    readonly_fields = ['get_preview', ]

    def get_preview(self, obj):
        if not obj.image:
            return 'Здесь будет превью, когда вы выберите файл.'
        return format_html(
            '<img src="{}" height=200px" />',
            obj.image.url,
        )


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [ImageInline, ]
    search_fields = ['title', ]
