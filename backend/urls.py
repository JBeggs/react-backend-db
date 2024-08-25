from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView
from rest_framework_simplejwt import views as jwt_views
from allauth.account.views import confirm_email


favicon_view = RedirectView.as_view(url="/static/favicon.ico", permanent=True)

urlpatterns = [

    path("api/", include("api.urls")),
    path('users/', include('users.urls')),
    path("admin/", admin.site.urls),
    path("favicon.ico", favicon_view),
    path("rest-auth/", include("dj_rest_auth.urls")),
    path("rest-auth-registration/", include("dj_rest_auth.registration.urls")),
    path("accounts/", include("allauth.urls")),
    path("token/", jwt_views.TokenObtainPairView.as_view(), name ="token_obtain_pair"),
    path("token/refresh/", jwt_views.TokenRefreshView.as_view(), name ="token_refresh"),

]

if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
