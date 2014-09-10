"""
Domain objects
"""
from django.db import models
from django.utils.text import slugify


class Page(models.Model):
    """
    Represents site's page
    """
    title = models.CharField(max_length=40, unique=True)
    slug = models.SlugField(max_length=40, unique=True)

    def __unicode__(self):
        return self.slug

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
    ordering = models.PositiveIntegerField(default=0)

    class Meta:
        abstract = True
        ordering = ('ordering',)


class DisplayType(models.Model):
    """
    Represents various display types
    """
    name = models.CharField(max_length=40, unique=True)
    code = models.CharField(max_length=5, unique=True)

    def __unicode__(self):
        return '%s - %s' % (self.code, self.name)


class Gallery(Section):
    """
    Represents photo-based section
    """
    slug = models.SlugField(max_length=100, unique=True)
    title = models.CharField(max_length=40, blank=True)
    description = models.TextField(max_length=3000, blank=True)

    # each gallery section has one display type
    display_type = models.ForeignKey(DisplayType)

    # instance owner
    page = models.ForeignKey(Page, related_name='galleries')

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        """
        Persists Gallery instance and initializes its ordering
        """
        super(Gallery, self).save(*args, **kwargs)

        # update ordering and generate slug
        if self.ordering == 0:
            self.ordering = self.id
            self.slug = '%s-%d' % (slugify(unicode(self.name)), self.id)
            self.save(update_fields=['ordering', 'slug'])

    def add_item(self, caption, summary='', description='', image=None):
        """
        Adds new gallery item

        Arguments:
        - `caption`: item caption
        - `summary`: item summary (optional)
        - `description`: item description (optional)
        - `image`: item image (optional)
        """
        values = {
            'caption': caption,
            'summary': summary,
            'description': description,
            'gallery': self
        }
        new_item = GalleryItem.objects.create(**values)

        # add photo if any provided
        if image:
            new_item.set_image(image)

    def remove_item(self, slug):
        """
        Removes slide from the presentation

        Method removes item if exists and returns True. If item does not
        exists, False is returned.

        Arguments:
        - `slug`: item's slug
        """
        item = self.items.filter(slug=slug)
        if item.exists():
            item.delete()
            return True

        return False

    class Meta(Section.Meta):
        verbose_name_plural = 'galleries'


class GalleryItem(models.Model):
    """
    Represents gallery section content
    """
    # main identifiers
    caption = models.CharField(max_length=40)
    slug = models.SlugField(max_length=100, unique=True)

    # miscellaneous data
    summary = models.CharField(max_length=140, blank=True)
    description = models.TextField(max_length=1500, blank=True)
    image = models.ForeignKey('photologue.Photo', null=True, blank=True)

    # instance owner
    gallery = models.ForeignKey(Gallery, related_name='items')

    def __unicode__(self):
        return self.slug

    def set_image(self, image):
        """
        Method sets item image

        Arguments:
        - `image`: Photo instance
        """
        self.image = image
        self.save(update_fields=['image'])

    def save(self, *args, **kwargs):
        """
        Persists GalleryItem instance and create its slug field
        """
        super(GalleryItem, self).save(*args, **kwargs)

        if not self.slug:
            self.slug = '%s-%d' % (slugify(unicode(self.caption)), self.id)
            self.save(update_fields=['slug'])


class Link(Section):
    """
    Represents linked section
    """
    url = models.URLField()
    local = models.BooleanField(default=False)

    # instance owner
    page = models.ForeignKey(Page, related_name='links')

    def save(self, *args, **kwargs):
        """
        Persists Link instance and initializes its ordering
        """
        super(Link, self).save(*args, **kwargs)

        # update ordering
        if self.ordering == 0:
            self.ordering = self.id
            self.save(update_fields=['ordering'])
