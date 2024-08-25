from django.contrib import admin

from .models import PageContent, PageGallery, Articles, ArticleGallery, Message, ContactMessage


class PageContentAdmin(admin.ModelAdmin):
    list_display = ("creator", "name", "title", 'created_at',)

class PageGalleryAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "image", "thumbnail", 'created_at',)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ("creator", "name", "title", 'created_at',)
    prepopulated_fields = {"slug": ["title"]}

class ArticleGalleryAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "image", "thumbnail", 'created_at',)

class MessageAdmin(admin.ModelAdmin):
    list_display = ("user", "article", "message", "created_at",)
    
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email_address", "contact_number", "message",)


admin.site.register(PageContent, PageContentAdmin)
admin.site.register(PageGallery, PageGalleryAdmin)

admin.site.register(Articles, ArticleAdmin)
admin.site.register(ArticleGallery, ArticleGalleryAdmin)

admin.site.register(Message, MessageAdmin)
admin.site.register(ContactMessage, ContactMessageAdmin)