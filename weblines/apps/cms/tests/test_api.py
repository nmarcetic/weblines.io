"""
API test suites
"""
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from weblines.apps.cms import models


class PageTests(APITestCase):
    """
    Page API test suite
    """
    def setUp(self):
        self.page = models.Page.objects.create(title='test page')

    def test_page_access(self):
        """
        Tests page retrieval

        Each page should be retrieved by its slug. In case of missing
        page, 404 should be returned. Successful retrievals has 200 as
        a response code.
        """
        # non-existent slug case
        url = reverse('pages-api', args={'invalid-slug', })
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        # valid request
        url = reverse('pages-api', args={'test-page', })
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
