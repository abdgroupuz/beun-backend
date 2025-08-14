from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Post(models.Model):
    image = models.ImageField(_("image"), upload_to="posts/")
    short_body_uz = models.TextField(_("short body uz"))
    short_body_ru = models.TextField(_("short body ru"))
    short_body_en = models.TextField(_("short body en"))
    body_uz = models.TextField(_("body uz"), blank=True)
    body_ru = models.TextField(_("body ru"), blank=True)
    body_en = models.TextField(_("body en"), blank=True)
    url = models.URLField(_("url"), blank=True)
    is_active = models.BooleanField(_("is active"), default=True)

    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)
    
    def __str__(self):
        return self.short_body_ru
    
    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")


class Certificate(models.Model):
    image = models.ImageField(_("image"), upload_to="certificates/")
    body_uz = models.TextField(_("body uz"))
    body_ru = models.TextField(_("body ru"))
    body_en = models.TextField(_("body en"))

    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)
    
    def __str__(self):
        return self.body_ru
    
    class Meta:
        verbose_name = _("Certificate")
        verbose_name_plural = _("Certificates")


class Star(models.Model):
    image = models.ImageField(_("image"), upload_to="starts/")
    full_name_uz = models.CharField(_("full name uz"), max_length=255)
    full_name_ru = models.CharField(_("full name ru"), max_length=255)
    full_name_en = models.CharField(_("full name en"), max_length=255)
    is_active = models.BooleanField(_("is active"), default=True)

    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)
    
    def __str__(self):
        return self.full_name_ru
    
    class Meta:
        verbose_name = _("Star")
        verbose_name_plural = _("Stars")


class Result(models.Model):
    image = models.ImageField(_("image"), upload_to="results/")

    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)
    
    class Meta:
        verbose_name = _("Result")
        verbose_name_plural = _("Results")


class Faq(models.Model):
    question_uz = models.TextField(_("question uz"))
    question_ru = models.TextField(_("question ru"))
    question_en = models.TextField(_("question en"))
    answer_uz = models.TextField(_("answer uz"))
    answer_ru = models.TextField(_("answer ru"))
    answer_en = models.TextField(_("answer en"))

    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)
    
    def __str__(self):
        return self.question_ru
    
    class Meta:
        verbose_name = _("FAQ")
        verbose_name_plural = _("FAQ")


class Banner(models.Model):
    source = models.FileField(
        _("source"),
        upload_to="banners/",
        validators=[
            FileExtensionValidator(
                allowed_extensions=["mp4", "webm", "mov", "jpg", "jpeg", "png", "gif"]
            )
        ],
    )
    source_md = models.FileField(
        _("source md"),
        upload_to="banners/",
        blank=True,
        null=True,
        validators=[
            FileExtensionValidator(
                allowed_extensions=["mp4", "webm", "mov", "jpg", "jpeg", "png", "gif"]
            )
        ],
    )
    source_sm = models.FileField(
         _("source sm"),
        upload_to="banners/",
        blank=True,
        null=True,
        validators=[
            FileExtensionValidator(
                allowed_extensions=["mp4", "webm", "mov", "jpg", "jpeg", "png", "gif"]
            )
        ],
    )
    url = models.URLField(_("url"), blank=True)
    is_active = models.BooleanField(_("is active"), default=True)

    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)

    def __str__(self):
        return self.source.name

    class Meta:
        verbose_name = _("Banner")
        verbose_name_plural = _("Banners")


class SpecialOffer(models.Model):
    product = models.ForeignKey("product.Product", on_delete=models.CASCADE)
    end_date = models.DateTimeField(_("end date"))
    photo = models.ImageField(_("photo"), upload_to="special_offers/")

    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)

    def __str__(self):
        return f"Special Offer for {self.product.name_en}"

    class Meta:
        verbose_name = _("Special Offer")
        verbose_name_plural = _("Special Offers")
