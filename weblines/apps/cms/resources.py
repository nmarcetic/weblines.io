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
        self.fields['links'] = Link(many=True)

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
        exclude = ('gallery',)


class Gallery(serializers.ModelSerializer):
    """
    Represents Gallery resource
    """
    items = GalleryItem(many=True)

    def transform_display_type(self, obj, value):
        """
        Use code as display type representation
        """
        return obj.display_type.code

    class Meta:
        model = models.Gallery
        exclude = ('id', 'page',)


class Link(serializers.ModelSerializer):
    """
    Represents Link resource
    """
    class Meta:
        model = models.Link
        exclude = ('id', 'page',)
