from django.db import models

# Create your models here.


class Post(models.Model):
    image = models.ImageField(upload_to="posts/")
    short_body_uz = models.TextField()
    short_body_ru = models.TextField()
    body_uz = models.TextField(blank=True)
    body_ru = models.TextField(blank=True)
    url = models.URLField(blank=True)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Certificate(models.Model):
    image = models.ImageField(upload_to="certificates/")
    body_uz = models.TextField()
    body_ru = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Star(models.Model):
    image = models.ImageField(upload_to="starts/")
    full_name_uz = models.CharField(max_length=255)
    full_name_ru = models.CharField(max_length=255)
    is_actve = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Result(models.Model):
    image = models.ImageField(upload_to="results/")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Faq(models.Model):
    question_uz = models.TextField()
    question_ru = models.TextField()
    answer_uz = models.TextField()
    answer_ru = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
