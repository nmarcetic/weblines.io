"""
Content-management app models
"""
from django.db import models
from django.utils.text import slugify


class Page(models.Model):
    """
    Represents site's page
    """
    title = models.CharField(max_length=40, unique=True)
    slug = models.SlugField(max_length=40, unique=True)

    def save(self, *args, **kwargs):
        """
        Persists a Page instance and creates its unique slug
        """
        if not self.slug:
            self.slug = slugify(unicode(self.title))

        super(Page, self).save(*args, **kwargs)


class Section(models.Model):
    """
    Abstract base class containing meta-data about section types
    """
    name = models.CharField(max_length=40, unique=True)
    title = models.CharField(max_length=40, blank=True)
    description = models.TextField(max_length=3000, blank=True)

    class Meta:
        abstract = True


class Gallery(Section):
    """
    Represents photo-based section
    """
    # TODO: add presentation info

    def add_item(self, name, summary='', description='', image=None):
        """
        Adds new gallery item

        Arguments:
        - `name`: item name
        - `summary`: item caption text (optional)
        - `description`: item description (optional)
        - `image`: item image (optional)
        """
        values = {
            'name': name,
            'summary': summary,
            'description': description,
            'gallery': self
        }
        new_item = GalleryItem.objects.create(**values)

        # add photo if any provided
        if image:
            new_item.set_image(image)

    def remove_item(self, name):
        """
        Removes slide from the presentation

        Method removes item if exists and returns True. If item does not
        exists, False is returned.

        Arguments:
        - `name`: item name
        """
        item = self.items.filter(name=name)
        if item.exists():
            item.delete()
            return True

        return False


class GalleryItem(models.Model):
    """
    Represents gallery section content
    """
    name = models.CharField(max_length=40, unique=True)
    summary = models.CharField(max_length=140, blank=True)
    description = models.TextField(max_length=1500, blank=True)
    image = models.ForeignKey('photologue.Photo', null=True, blank=True)

    # instance owner
    gallery = models.ForeignKey(Gallery, related_name='items')

    def set_image(self, image):
        """
        Method sets item image

        Arguments:
        - `image`: Photo instance
        """
        self.image = image
        self.save(update_fields=['image'])


class Link(Section):
    """
    Represents linked section
    """
    url = models.URLField()
    local = models.BooleanField(default=False)
