import os
from django.conf import settings
from django.template.defaultfilters import slugify
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError
from django.contrib.sites.models import Site
from content.models import PageContent, Articles
from content.models import process_content_file


User = get_user_model()


class Command(BaseCommand):
    help = "Import Articles from CSV"

    def handle(self, *args, **options):
        pages = ['home', 'about', "article"]

        exists = Site.objects.all()
        for site in exists:
            site.name = "Free Article publishing"
            site.domain = "articlesharing.com"
            site.save()

        for page in pages:
            
            exists = PageContent.objects.filter(page=page)
            if not exists:
                content = PageContent()
                content.creator = User.objects.get(username="admin")
                content.name = page.title()
                content.page = page
                content.title = "Free Article publishing"
                content.title_description = "articlesharing.com."
                content.paragraph_1 = "This is a site that tries to be inline editatble. When you own the article or are the logged in as the Site Admin, you can edit the content."
                content.paragraph_2 = "Please change me use ... for an empty line"
                content.paragraph_3 = "This is your timeline, create a good one."
                content.paragraph_4 = "Share the news you find interesting."
                content.paragraph_5 = "Please change me use ... for an empty line"
                content.active = True
                content.save()

        file_path = os.path.join(settings.BASE_DIR, 'static/articles/article_database.xlsx')
        csv_file = open(file_path, "r")
        process_content_file(file_path)
        # csv = file.p[em]
