from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Item(models.Model):
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE, verbose_name=_("product"))
    count = models.IntegerField(_("count"))
    price = models.DecimalField(_("price"), max_digits=10, decimal_places=2)

    def __str__(self):
        return self.product.name + ' - ' + str(self.count)
    
    class Meta:
        verbose_name = _("Item")
        verbose_name_plural = _("Items")


class Cart(models.Model):
    user = models.OneToOneField('user.User', on_delete=models.CASCADE, verbose_name=_("user"))
    products = models.ManyToManyField(Item, verbose_name=_("products"))

    def __str__(self):
        return f"{self.user.phone}'s cart"
    
    class Meta:
        verbose_name = _("Cart")
        verbose_name_plural = _("Carts")


class Order(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Processing', 'Processing'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled')
    )
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, verbose_name=_("user"))
    products = models.ManyToManyField(Item, related_name='orders', verbose_name=_("products"))
    total_price = models.DecimalField(_("total price"), max_digits=10, decimal_places=2)
    amount = models.IntegerField(_("amount"))
    description = models.TextField(_("description"), blank=True, null=True)

    delivery = models.BooleanField(_("delivery"), default=True)
    address = models.ForeignKey('user.Address', on_delete=models.CASCADE, null=True, verbose_name=_("address"))
    status = models.CharField(_("status"), max_length=15, default='Pending', choices=STATUS_CHOICES)

    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)

    def __str__(self):
        return f"{self.user.phone}'s order #{self.pk}"
    
    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")
