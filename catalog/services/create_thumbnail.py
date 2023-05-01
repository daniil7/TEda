
from django.conf import settings
from PIL import Image
import os

def createThumbnail(image_path):
    try:
        image = Image.open(image_path)
    except:
        return False
    image.thumbnail((360,360), Image.ANTIALIAS)
    image_filename = os.path.basename(image_path)
    thumb_name, thumb_extension = os.path.splitext(image_filename)
    thumb_extension = thumb_extension.lower()

    if thumb_extension in ['.jpg', '.jpeg']:
        FTYPE = 'JPEG'
    elif thumb_extension == '.gif':
        FTYPE = 'GIF'
    elif thumb_extension == '.png':
        FTYPE = 'PNG'
    else:
        return False    # Unrecognized file type

    return image
