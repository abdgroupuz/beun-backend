from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Category(models.Model):
    name_uz = models.CharField(_("name uz"), max_length=255)
    name_ru = models.CharField(_("name ru"), max_length=255)
    name_en = models.CharField(_("name en"), max_length=255)
    image = models.ImageField(_("image"), upload_to="category/", null=True, blank=True)
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)
    parent = models.ForeignKey("self", related_name="childrens", on_delete=models.CASCADE, null=True, blank=True, verbose_name=_("parent"))

    def __str__(self):
        return self.name_ru
    
    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")


class Tag(models.Model):
    name_uz = models.CharField(_("name uz"), max_length=255)
    name_ru = models.CharField(_("name ru"), max_length=255)
    name_en = models.CharField(_("name en"), max_length=255)
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)

    def __str__(self):
        return self.name_ru
    
    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")


class Image(models.Model):
    STATUS_CHOICES = (
        ('M', 'Main'),
        ('A', 'Additional'),
    )
    source = models.FileField(_("Product Image"), upload_to='products/')
    status = models.TextField(_("Product Image Status"), choices=STATUS_CHOICES, max_length=1)

    def __str__(self):
        return str(self.pk) + ' ' + self.status
    
    class Meta:
        verbose_name = _("Image")
        verbose_name_plural = _("Images")


class Product(models.Model):
    spu = models.CharField(max_length=255, blank=True, null=True)
    name_uz = models.CharField(_("name uz"), max_length=255)
    name_ru = models.CharField(_("name ru"), max_length=255)
    name_en = models.CharField(_("name en"), max_length=255)
    short_description_uz = models.TextField(_("short description uz"), )
    short_description_ru = models.TextField(_("short description ru"), )
    short_description_en = models.TextField(_("short description en"), )
    description_uz = models.TextField(_("description uz"),)
    description_ru = models.TextField(_("description ru"),)
    description_en = models.TextField(_("description en"),)

    category = models.ForeignKey(Category, related_name="products", on_delete=models.CASCADE, verbose_name=_("Category"))
    tags = models.ManyToManyField(Tag, related_name='products', blank=True, verbose_name=_("Tags"))

    price = models.DecimalField(_("price"), max_digits=10, decimal_places=2)
    discount = models.SmallIntegerField(_("discount"), blank=True, null=True)
    discounted_price = models.DecimalField(_("discounted price"), max_digits=10, decimal_places=2, blank=True, null=True)

    images = models.ManyToManyField(Image, related_name='products', verbose_name=_("Images"))

    count = models.IntegerField(_("count"),)
    hit_count = models.IntegerField(_("hit count"), default=0)
    sold_count = models.IntegerField(_("sold count"), default=0)

    is_active = models.BooleanField(_("is active"), default=True)
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)

    def __str__(self):
        return self.name_ru

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")