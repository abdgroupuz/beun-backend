from django.utils.translation import gettext_lazy as _
from rest_framework import views, status, permissions, generics, viewsets
from rest_framework.response import Response
from dj_rest_auth.app_settings import api_settings
from dj_rest_auth.jwt_auth import set_jwt_cookies
from dj_rest_auth.utils import jwt_encode
from dj_rest_auth.jwt_auth import JWTCookieAuthentication

from api.v1.serializers.user import VerifyPhoneSerializer, VerifySerializer, AddressSerializer
from api.v1.permissions import IsAdminOrIsOwner
from apps.user.models import Address


class SendVerificationView(views.APIView):
    permission_classes = (permissions.AllowAny,)
    allowed_methods = ('POST', 'OPTIONS', 'HEAD')

    def get_serializer(self, *args, **kwargs):
        return VerifyPhoneSerializer(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        sms = serializer.save()
        # sendSMS.delay(sms.phone, sms.code)
        return Response(
                    {'detail': _('The verification code has been sent')},
                    status=status.HTTP_200_OK
                )


class VerifyView(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny,)
    allowed_methods = ('POST', 'OPTIONS', 'HEAD')
    serializer_class = VerifySerializer

    user = None
    access_token = None
    token = None 

    def get_response(self):
        serializer_class = api_settings.JWT_SERIALIZER

        data = {
            'user': self.user,
            'access': self.access_token,
            'refresh': self.refresh_token,
        }

        serializer = serializer_class(
            instance=data,
            context=self.get_serializer_context(),
        )

        response = Response(serializer.data, status=status.HTTP_200_OK)
        set_jwt_cookies(response, self.access_token, self.refresh_token)
        return response

    def post(self, request, *args, **kwargs):
        self.request = request
        serializer = VerifySerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)

        self.user = serializer.save()

        self.access_token, self.refresh_token = jwt_encode(self.user)
        return self.get_response()


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = (IsAdminOrIsOwner,)
    authentication_classes = (JWTCookieAuthentication,)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user.id)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
