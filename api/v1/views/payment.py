from payme.views import PaymeWebHookAPIView
from click_up.views import ClickWebhook

from apps.market.models import Order


class PaymeCallBackAPIView(PaymeWebHookAPIView):
    def handle_created_payment(self, params, result, *args, **kwargs):
        """
        Handle the successful payment. You can override this method
        """
        print(f"Transaction created for this params: {params} and cr_result: {result}")

    def handle_successfully_payment(self, params, result, *args, **kwargs):
        """
        Handle the successful payment. You can override this method
        """
        order = Order.objects.filter(pk=params.get("order_id")).first()
        if order:
            order.status = "Processing"
            order.save()
        print(f"Transaction successfully performed for this params: {params} and performed_result: {result}")

    def handle_cancelled_payment(self, params, result, *args, **kwargs):
        """
        Handle the cancelled payment. You can override this method
        """
        order = Order.objects.filter(pk=params.get("order_id")).first()
        if order:
            order.status = "Cancelled"
            order.save()
        print(f"Transaction cancelled for this params: {params} and cancelled_result: {result}")


class ClickWebhookAPIView(ClickWebhook):
    def successfully_payment(self, params):
        """
        successfully payment method process you can ovveride it
        """
        order = Order.objects.filter(pk=params.get("order_id")).first()
        if order:
            order.status = "Processing"
            order.save()
        print(f"payment successful params: {params}")

    def cancelled_payment(self, params):
        """
        cancelled payment method process you can ovveride it
        """
        order = Order.objects.filter(pk=params.get("order_id")).first()
        if order:
            order.status = "Cancelled"
            order.save()
        print(f"payment cancelled params: {params}")
