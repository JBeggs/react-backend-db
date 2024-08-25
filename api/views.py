from django.middleware.csrf import get_token 
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from content.models import PageContent, PageGallery, Articles, ArticleGallery


# Create your views here.
@csrf_exempt
def site_info(request, *args, **kwargs):
    home = list(PageContent.objects.filter(page="home").values())
    home_gallery = list(PageGallery.objects.filter(page__page="home").values())
    about = list(PageContent.objects.filter(page="about").values())
    about_gallery = list(PageGallery.objects.filter(page__page="about").values())
    articlepage = list(PageContent.objects.filter(page="article").values())
    article_gallery = list(PageGallery.objects.filter(page__page="article").values())
    
    articles = list(Articles.objects.filter(active=True).values(
        "id", "creator", "name", "title", "title_description", "hero_image", "slug", "link", "category",
        "paragraph_1", "paragraph_2", "paragraph_3", "paragraph_4", "paragraph_5", "paragraph_6", "paragraph_7",
        "header_1", "header_2", "header_3", "header_4", "header_5",
        "file", "created_at", "updated_at", "active", "hero_image",
        "creator__first_name", "creator__last_name", "creator__username"
    ))
    
    articles_gallery = list(ArticleGallery.objects.filter().values())
    
    return JsonResponse(
        {
            "csrf_token": get_token(request),
            "home": home,
            "home_gallery": home_gallery,
            "about": about,
            "about_gallery": about_gallery,
            "articlepage": articlepage,
            "article_gallery": article_gallery,
            "articles" : articles,
            "articles_gallery" : articles_gallery,
        }
    )