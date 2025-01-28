from django.db import models

# Create your models here.

class Category(models.Model):
    name_uz = models.CharField(max_length=255)
    name_ru = models.CharField(max_length=255)
    image = models.ImageField(upload_to="category/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name_ru


class Tag(models.Model):
    name_uz = models.CharField(max_length=255)
    name_ru = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name_ru


class Image(models.Model):
    STATUS_CHOICES = (
        ('M', 'Main'),
        ('A', 'Additional'),
    )
    source = models.FileField(upload_to='products/')
    status = models.TextField(choices=STATUS_CHOICES, max_length=1)

    def __str__(self):
        return self.pk + ' ' + self.status


class Product(models.Model):
    spu = models.CharField(max_length=255, blank=True, null=True)
    name_uz = models.CharField(max_length=255)
    name_ru = models.CharField(max_length=255)
    short_description_uz = models.TextField()
    short_description_ru = models.TextField()
    description_uz = models.TextField()
    description_ru = models.TextField()

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    tags = models.ManyToManyField(Tag, related_name='products', blank=True)

    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.SmallIntegerField(blank=True, null=True)
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    images = models.ManyToManyField(Image, related_name='products')

    count = models.IntegerField()
    hit_count = models.IntegerField(default=0)
    sold_count = models.IntegerField(default=0)

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name_ru
