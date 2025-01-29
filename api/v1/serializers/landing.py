from rest_framework import serializers
from apps.landing.models import Certificate, Faq, Post, Result, Star


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = "__all__"


class FaqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faq
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = "__all__"


class StarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Star
        fields = "__all__"
