from django.db import models

# Create your models here.


class Item(models.Model):
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE)
    count = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.product.name + ' - ' + str(self.count)


class Cart(models.Model):
    user = models.OneToOneField('user.User', on_delete=models.CASCADE)
    products = models.ManyToManyField(Item)

    def __str__(self):
        return f"{self.user.phone}'s cart"


class Order(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Processing', 'Processing'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled')
    )
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    products = models.ManyToManyField(Item, related_name='orders')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.IntegerField()
    description = models.TextField()

    delivery = models.BooleanField(default=True)
    address = models.ForeignKey('user.Address', on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=15, default='Pending', choices=STATUS_CHOICES)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.phone}'s order #{self.pk}"
