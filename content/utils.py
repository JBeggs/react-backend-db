from io import BytesIO

from django.core.files.base import ContentFile
from django.template.defaultfilters import slugify
from PIL import Image
import pandas as pd


def create_thumbnail(img, thumb, w, h):

    if not img:
        return

    image = Image.open(img.file).convert('RGB')
    # If the image is smaller than w x h, don't bother creating a thumbnail.
    width, height = image.size
    if width < w or height < h:
        return
    # Crop as little as possible to square, keeping the center.
    if width > height:
        delta = width - height
        left = int(delta / 2)
        upper = 0
        right = height + left
        lower = height
    else:
        delta = height - width
        left = 0
        upper = int(delta / 2)
        right = width
        lower = width + upper
    image = image.crop((left, upper, right, lower))
    # Create the thumbnail as a w x h square.
    image.thumbnail((w, h), Image.Resampling.LANCZOS)
    # Save the thumbnail in the FileField.
    # Using Image.save(content, 'jpeg') seems to work for png too.
    buffer = BytesIO()
    image.save(buffer, 'jpeg', quality=95)
    cf = ContentFile(buffer.getvalue())
    thumb.save(name=img.name, content=cf, save=False)
    
    
def image_thumbnail_path(instance, filename):
    if '/' in filename:
        filename = filename.split('/')[-1]
    ext = filename.split('.')[-1]
    return f'page/thumb/{slugify(instance.page.id)}/{slugify(instance.name)}.{ext}'


def article_gallery_image_thumbnail_path(instance, filename):
    if '/' in filename:
        filename = filename.split('/')[-1]
    ext = filename.split('.')[-1]
    return f'page/thumb/{slugify(instance.article.id)}/{slugify(instance.name)}.{ext}'


def page_file_path(instance, filename):
    if '/' in filename:
        filename = filename.split('/')[-1]
    ext = filename.split('.')[-1]
    return f'page/file/{slugify(instance.creator.id)}/{slugify(instance.name)}.{ext}'

def article_file_path(instance, filename):
    if '/' in filename:
        filename = filename.split('/')[-1]
    ext = filename.split('.')[-1]
    return f'article/file/{slugify(instance.creator.id)}/{slugify(instance.name)}.{ext}'

def page_image_path(instance, filename):
    if '/' in filename:
        filename = filename.split('/')[-1]
    ext = filename.split('.')[-1]
    return f'page/image/{slugify(instance.creator.id)}/{slugify(instance.name)}.{ext}'


def page_gallery_image_path(instance, filename):
    if '/' in filename:
        filename = filename.split('/')[-1]
    ext = filename.split('.')[-1]
    return f'page/gallery/image/{slugify(instance.page.id)}/{slugify(instance.name)}.{ext}'


def article_image_path(instance, filename):
    if '/' in filename:
        filename = filename.split('/')[-1]
    ext = filename.split('.')[-1]
    return f'article/image/{slugify(instance.creator.id)}/{slugify(instance.name)}.{ext}'


def article_gallery_image_path(instance, filename):
    if '/' in filename:
        filename = filename.split('/')[-1]
    ext = filename.split('.')[-1]
    return f'article/gallery/image/{slugify(instance.article.id)}/{slugify(instance.name)}.{ext}'