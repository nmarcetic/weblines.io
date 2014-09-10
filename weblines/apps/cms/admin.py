"""
Admin panel configuration
"""
from django.contrib import admin
from weblines.apps.cms import models


class DisplayType(admin.ModelAdmin):
    """
    DisplayType model customizations
    """
    list_display = ('name', 'code')


class GalleryInline(admin.StackedInline):
    """
    Gallery model customizations
    """
    model = models.Gallery
    exclude = ('slug',)
    extra = 0


class Page(admin.ModelAdmin):
    """
    Page model customisations
    """
    inlines = [GalleryInline, ]
    exclude = ('slug',)

    list_display = ('title', 'slug')


# register customized models
admin.site.register(models.Page, Page)
admin.site.register(models.DisplayType, DisplayType)
