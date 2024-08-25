from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.utils.translation import gettext as _
from django.contrib.auth import get_user_model
from django.views.generic import FormView, UpdateView, TemplateView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import (
    RetrieveAPIView,
    GenericAPIView,
    RetrieveUpdateAPIView,
)
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework import permissions, viewsets, filters

from .models import Address, PhoneNumber, Profile
from .permissions import IsUserAddressOwner, IsUserProfileOwner
from .serializers import (
    AddressReadOnlySerializer,
    PhoneNumberSerializer,
    ProfileSerializer,
    UserSerializer,
    VerifyPhoneNumberSerialzier
)
from .form import PhoneNumberForm, ProfileForm, AddressForm

User = get_user_model()


class SendOrResendSMSAPIView(GenericAPIView):
    """
    Check if submitted phone number is a valid phone number and send OTP.
    """
    serializer_class = PhoneNumberSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    permission_classes = []
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Send OTP
            phone_number = str(serializer.validated_data['phone_number'])

            user = User.objects.filter(
                phone__phone_number=phone_number).first()

            sms_verification = PhoneNumber.objects.filter(
                user=user, is_verified=False).first()

            sms_verification.send_confirmation()

            return Response(status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyPhoneNumberAPIView(GenericAPIView):
    """
    Check if submitted phone number and OTP matches and verify the user.
    """
    serializer_class = VerifyPhoneNumberSerialzier
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    permission_classes = []
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            message = {'detail': _('Phone number successfully verified.')}
            return Response(message, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileViewSet(viewsets.ModelViewSet):
    """
    Get, Update user profile
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    permission_classes = []


class UserViewSet(viewsets.ModelViewSet):
    """
    Get, Update user
    """
    search_fields = ["username"]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    permission_classes = []

    def list(self, request):
        filter = filters.SearchFilter()
        queryset = filter.filter_queryset(request, User.objects.all(), self) 
        serializer = UserSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)


class AddressViewSet(viewsets.ModelViewSet):
    """
    List and Retrieve user addresses
    """
    queryset = Address.objects.all()
    serializer_class = AddressReadOnlySerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    permission_classes = []
