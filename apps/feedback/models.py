from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.user.models import User
from apps.product.models import Product

# Create your models here.

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', verbose_name=_("user"))
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments', verbose_name=_("product"))
    reply_to = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies', verbose_name=_("reply to"))
    rate = models.SmallIntegerField(_("rate"))

    text = models.TextField(_("text"))
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)

    def __str__(self):
        return self.text
    
    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")


class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='feedbacks', verbose_name=_("user"))
    phone = models.CharField(_("phone"), max_length=20)
    full_name = models.CharField(_("full name"), max_length=255)
    text = models.TextField(_("text"))
    created_at = models.DateTimeField(_("updated at"), auto_now_add=True)

    def __str__(self):
        return self.text
    
    class Meta:
        verbose_name = _("Feedback")
        verbose_name_plural = _("Feedbacks")
