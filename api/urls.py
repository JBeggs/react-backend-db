from django.contrib import admin

from django.urls import include, path
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import site_info
from content.views import PageContentViewSet, PageGalleryViewSet, ArticlesViewSet, ArticleGalleryViewSet, MessageViewSet, ContactMessageViewSet

admin.autodiscover()

router = DefaultRouter()
router.register(r'update/page', PageContentViewSet)
router.register(r'update/pagegallery', PageGalleryViewSet)
router.register(r'update/article', ArticlesViewSet)
router.register(r'update/articlegallery', ArticleGalleryViewSet)
router.register(r'update/message', MessageViewSet)
router.register(r'update/contact', ContactMessageViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path(r'info/',      site_info, name='build'),
]
