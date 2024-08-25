from django.contrib.auth import get_user_model
from django.db import models
from django.template.defaultfilters import truncatechars
from django.template.defaultfilters import slugify
from django.utils.safestring import mark_safe
from django.utils.translation import gettext as _

from .utils import create_thumbnail, image_thumbnail_path, page_file_path, article_file_path, page_image_path, page_gallery_image_path, article_image_path, article_gallery_image_path, article_gallery_image_thumbnail_path
import pandas as pd


User = get_user_model()


def process_content_file(file):
    if file:
        df = pd.read_excel(file, header=1)

        current_articles = Articles.objects.all()
        for article in current_articles:
            article.delete()

        n = 0
        for index, data in df.iterrows():

            if type(data["name"]) != float:

                content = Articles()
                content.name = data['name']
                content.title = data['title']
                content.title_description = data['title_description']

                content.header_1 = data['header_1']

                content.header_2 = data['header_2']
                content.header_3 = data['header_3']
                content.header_4 = data['header_4']
                content.header_5 = data['header_5']

                content.paragraph_1 = data['paragraph_1']
                content.paragraph_2 = data['paragraph_2']
                content.paragraph_3 = data['paragraph_3']
                content.paragraph_4 = data['paragraph_4']
                content.paragraph_5 = data['paragraph_5']
                content.paragraph_6 = data['paragraph_6']
                content.paragraph_7 = data['paragraph_7']
                
                content.active = data['active']

                content.link = data['link']
                
                user = User()
                user = User.objects.filter(username=data['username'])
                if not user:
                    user = User()
                    user.username = data['username']

                    user.first_name = data['first_name']
                    user.last_name = data['last_name']
                    user.set_password("Defcon12")
                    user.save()

                else:
                    user = user[0]
                    
                content.creator = user
                content.save()

                n += 1


class PageContent(models.Model):

    creator = models.ForeignKey(
        User, related_name="page_creator", on_delete=models.CASCADE)

    PAGE_CHOICES = [
        ('home', 'Home'),
        ('about', 'About'),
        ('contact', 'Contact'),
        ('article', 'Article'),
        # add more options here
    ]
    name = models.CharField(max_length=200, blank=True, null=True)
    page = models.CharField(max_length=200, choices=PAGE_CHOICES, blank=True)
    title = models.CharField(max_length=500, blank=True, null=True)
    title_description = models.TextField(_('Title Description'), blank=True)
    hero_image = models.ImageField(upload_to=page_image_path, blank=True, max_length=300)
    
    paragraph_1 = models.TextField(_('paragraph'), blank=True)
    paragraph_2 = models.TextField(_('paragraph'), blank=True)
    paragraph_3 = models.TextField(_('paragraph'), blank=True)
    paragraph_4 = models.TextField(_('paragraph'), blank=True)
    paragraph_5 = models.TextField(_('paragraph'), blank=True)
    paragraph_6 = models.TextField(_('paragraph'), blank=True)
    paragraph_7 = models.TextField(_('paragraph'), blank=True)
    file = models.FileField(upload_to=page_file_path, blank=True, null=True)
    active     = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('-created_at', )

    def __str__(self):
        return f"{self.name}"

    def save(self):
        if bool(self.file.name) and self.file.storage.exists(self.file.name):
            process_content_file(self.file.path)
        super(PageContent, self).save()


class PageGallery(models.Model):
    page = models.ForeignKey(
        PageContent, related_name="page_gallery", on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to=page_gallery_image_path, blank=True, max_length=300)
    description = models.CharField(max_length=200, blank=True)
    thumbnail = models.ImageField(upload_to=image_thumbnail_path, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('-created_at', )

    def __str__(self):
        return f"{self.name}"

    def save(self):
        create_thumbnail(self.image, self.thumbnail, 200, 200)
        super(PageGallery, self).save()

    @property
    def short_description(self):
        return truncatechars(self.description, 60)

    def image_tag(self):
        from django.utils.html import escape
        try:
            return mark_safe(u'<img src="%s" />' % escape(self.thumbnail.url))
        except:
            try:
                return mark_safe(u'<img style="height:200px;" src="%s" />' % escape(self.image.url))
            except:
                return ''


class Articles(models.Model):

    creator = models.ForeignKey(
        User, related_name="article_creator", on_delete=models.CASCADE)

    category = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    title = models.CharField(max_length=500, blank=True, null=True)
    slug = models.SlugField(default="", null=False)
    title_description = models.TextField(_('Title Description'), blank=True, null=True)
    hero_image = models.ImageField(upload_to=article_image_path, blank=True, max_length=300)

    header_1 = models.CharField(max_length=200, blank=True, null=True)
    paragraph_1 = models.TextField(_('paragraph'), blank=True, null=True)
    header_2 = models.CharField(max_length=200, blank=True, null=True)
    paragraph_2 = models.TextField(_('paragraph'), blank=True, null=True)
    header_3 = models.CharField(max_length=200, blank=True, null=True)
    paragraph_3 = models.TextField(_('paragraph'), blank=True, null=True)
    header_4 = models.CharField(max_length=200, blank=True, null=True)
    paragraph_4 = models.TextField(_('paragraph'), blank=True, null=True)
    header_5 = models.CharField(max_length=200, blank=True, null=True)
    paragraph_5 = models.TextField(_('paragraph'), blank=True, null=True)
    paragraph_6 = models.TextField(_('paragraph'), blank=True, null=True)
    paragraph_7 = models.TextField(_('paragraph'), blank=True, null=True)
    
    link = models.CharField(max_length=500, blank=True, null=True)
    file = models.FileField(upload_to=article_file_path, blank=True, null=True)
    active     = models.BooleanField(default=False, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def creator_username(self):
        return f"{self.creator.username}"

    class Meta:
        ordering = ('-created_at', )

    def __str__(self):
        return f"{self.name}"
    
    def save(self):
        if not self.name:
            self.name = "Blank"
        self.slug = slugify(self.name[:33])
        super(Articles, self).save()


class ArticleGallery(models.Model):
    article = models.ForeignKey(
        Articles, related_name="article_gallery", on_delete=models.CASCADE)
    
    name = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to=article_gallery_image_path, blank=True, max_length=300)
    description = models.CharField(max_length=200, blank=True)
    thumbnail = models.ImageField(upload_to=article_gallery_image_thumbnail_path, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('-created_at', )

    def __str__(self):
        return f"{self.name}"

    def save(self):
        create_thumbnail(self.image, self.thumbnail, 200, 200)
        super(ArticleGallery, self).save()

    @property
    def short_description(self):
        return truncatechars(self.description, 60)


class Message(models.Model):
    user = models.ForeignKey(
        User, related_name="user_message", on_delete=models.CASCADE)
    article = models.ForeignKey(
        Articles, related_name="article_message", on_delete=models.CASCADE)
    message_id = models.ForeignKey(
        'self', related_name="related_message", on_delete=models.CASCADE, blank=True, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.message}"
    
    

class ContactMessage(models.Model):
    first_name = models.CharField(max_length=128, blank=True, null=True)
    last_name = models.CharField(max_length=128, blank=True, null=True)
    email_address = models.EmailField(max_length=200, blank=True, null=True)
    contact_number = models.CharField(max_length=128, blank=True, null=True)

    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.message}"
