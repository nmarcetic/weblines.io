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


class GalleryItem(admin.StackedInline):
    """
    GalleryItem model customizations
    """
    model = models.GalleryItem
    exclude = ('slug',)
    extra = 0


class Gallery(admin.ModelAdmin):
    """
    Gallery model customization
    """
    inlines = [GalleryItem, ]


class Link(admin.StackedInline):
    """
    Link model customization
    """
    model = models.Link
    extra = 0


class Page(admin.ModelAdmin):
    """
    Page model customisations
    """
    inlines = [Link, ]
    exclude = ('slug',)
    list_display = ('title', 'slug')


# register customized models
admin.site.register(models.Page, Page)
admin.site.register(models.DisplayType, DisplayType)
admin.site.register(models.Gallery, Gallery)
