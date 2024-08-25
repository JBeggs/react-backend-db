from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    AddressViewSet,
    ProfileViewSet,
    UserViewSet,
    SendOrResendSMSAPIView,
    VerifyPhoneNumberAPIView,
)

app_name = "users"

router = DefaultRouter()
router.register(r"address", AddressViewSet)
router.register(r"user", UserViewSet)
router.register(r"profile", ProfileViewSet)

urlpatterns = [

    path(
        "send-sms/",
        SendOrResendSMSAPIView.as_view(),
        name="send_resend_sms"
    ),
    path(
        "verify-phone/",
        VerifyPhoneNumberAPIView.as_view(),
        name="verify_phone_number"
    ),

    path("", include(router.urls)),

]
