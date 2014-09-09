"""
Content-management app resources representations
"""
from rest_framework import serializers

from weblines.apps.cms import models


class Page(serializers.ModelSerializer):
    """
    Represents Page resource
    """
    class Meta:
        model = models.Page


class GalleryItem(serializers.ModelSerializer):
    """
    Represents GalleryItem resource
    """
    class Meta:
        model = models.GalleryItem


class Gallery(serializers.ModelSerializer):
    """
    Represents Gallery resource
    """
    items = GalleryItem(many=True)

    class Meta:
        model = models.Gallery
