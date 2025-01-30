from django.urls import path
from rest_framework.routers import DefaultRouter
from api.v1.views.user import SendVerificationView, VerifyView, AddressViewSet


router = DefaultRouter()
router.register("user/address", AddressViewSet, basename="address")

urlpatterns = [
    path("user/send_code", SendVerificationView.as_view(), name="send-verification"),
    path("user/verify/", VerifyView.as_view(), name="verify"),
] + router.urls
