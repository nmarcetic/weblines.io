"""
Resources representations
"""
from rest_framework import serializers
from weblines.apps.cms import models


class Page(serializers.ModelSerializer):
    """
    Represents Page resource
    """
    def __init__(self, *args, **kwargs):
        super(Page, self).__init__(*args, **kwargs)

        # add serializer fields
        self.fields['galleries'] = Gallery(many=True)

    class Meta:
        model = models.Page
        exclude = ('id',)


class GalleryItem(serializers.ModelSerializer):
    """
    Represents GalleryItem resource
    """
    # TODO: create image property
    class Meta:
        model = models.GalleryItem


class Gallery(serializers.ModelSerializer):
    """
    Represents Gallery resource
    """
    items = GalleryItem(many=True)

    class Meta:
        model = models.Gallery
