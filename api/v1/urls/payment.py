from django.urls import path

from api.v1.views.payment import PaymeCallBackAPIView, ClickWebhookAPIView


urlpatterns = [
    path('payment/payme/callback/', PaymeCallBackAPIView.as_view(), name='payme-callback'),
    path('payment/click/callback/', ClickWebhookAPIView.as_view(), name='click-callback'),
]
