"""
Content-management API
"""
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

from weblines.apps.cms import resources
from weblines.apps.cms import models


class PagesAPI(viewsets.ModelViewSet):
    """
    Page resource access methods
    """
    def retrieve(self, request, slug):
        """
        Retrieves page instance

        Page instance is identified via provided slug value.

        Arguments:
        - `request`: HTTP request
        - `slug`: Page slug
        """
        page = get_object_or_404(models.Page, slug=slug)
        response_data = resources.Page(page)
        return Response(response_data, status=status.HTTP_200_OK)
