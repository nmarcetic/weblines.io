"""
Domain objects test suites
"""
from django.db import IntegrityError
from django.test import TestCase

from weblines.apps.cms import models


class PageTestCase(TestCase):
    """
    Contains page-related test scenarios
    """
    def test_creation(self):
        """
        Tests various creation scenarios

        Each object is assigned unique slug, generated from its title. Once
        created, slug retains its value even when page title is updated.
        """
        # object creation
        new_page = models.Page.objects.create(title='First page')
        self.assertEqual(new_page.slug, 'first-page')
        self.assertEqual(new_page.id, 1)

        # title update
        new_page.title = 'Different title'
        new_page.save(update_fields=['title'])
        self.assertEqual(new_page.slug, 'first-page')

        # slug duplication
        with self.assertRaises(IntegrityError):
            models.Page.objects.create(title='First  page')


class GalleryTestCase(TestCase):
    """
    Contains gallery-related test scenarios
    """
    def setUp(self):
        """
        Creates dummy gallery
        """
        # create owner page
        page = models.Page.objects.create(title='first page')

        # create new display type
        display_type = models.DisplayType.objects.create(name='gallery',
                                                         code='G')

        # instantiate gallery and bind it to a created display type
        self.gallery = models.Gallery.objects.create(name='slider',
                                                     page=page,
                                                     display_type=display_type)

    def test_item_addition(self):
        """
        Tests item addition
        """
        self.gallery.add_item('gallery-item')
        self.assertEqual(1, self.gallery.items.count())
        self.assertEqual('gallery-item', self.gallery.items.first().caption)

        # in case of same captions, slugs must remain unique
        self.gallery.add_item('gallery-item')
        first = self.gallery.items.first()
        last = self.gallery.items.last()
        self.assertNotEqual(first.slug, last.slug)

    def test_item_removal(self):
        """
        Tests item removal

        Gallery item is removed if its name is found in added items.
        """
        self.test_item_addition()
        self.assertEqual(2, self.gallery.items.count())

        # failed search should result with False
        return_value = self.gallery.remove_item('invalid-item')
        self.assertEqual(False, return_value)

        # successful search should remove item and return True
        return_value = self.gallery.remove_item('gallery-item-1')
        self.assertEqual(True, return_value)
        self.assertEqual(1, self.gallery.items.count())

        # slide should be completely removed from system
        self.assertEqual(1, models.GalleryItem.objects.count())
