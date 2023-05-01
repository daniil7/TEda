from django.test import TestCase
from django.conf import settings
import os


# Create your tests here.

from catalog.services.create_thumbnail import createThumbnail

class ThumbnailTestCase(TestCase):
#    def setUp(self):
#        Animal.objects.create(name="lion", sound="roar")

    def test_thumbnail_creating(self):

        self.assertNotEqual( \
              createThumbnail( \
                  os.path.join( \
                      settings.BASE_DIR, \
                      'catalog/tests/test_thumbnails/image.jpeg'
                  )
              ), \
           False)
