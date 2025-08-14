from rest_framework.viewsets import ReadOnlyModelViewSet, GenericViewSet
from rest_framework.mixins import ListModelMixin

from api.v1.serializers.landing import (
    CertificateSerializer,
    FaqSerializer,
    PostSerializer,
    ResultSerializer,
    StarSerializer,
    BannerSerializer,
    SpecialOfferSerializer
)
from apps.landing.models import Certificate, Faq, Post, Result, Star, Banner, SpecialOffer


class CertificateViewSet(ReadOnlyModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer


class FaqViewSet(ReadOnlyModelViewSet):
    queryset = Faq.objects.all()
    serializer_class = FaqSerializer


class PostViewSet(ReadOnlyModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class ResultViewSet(ReadOnlyModelViewSet):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer


class StarViewSet(ReadOnlyModelViewSet):
    queryset = Star.objects.all()
    serializer_class = StarSerializer


class BannerViewSet(GenericViewSet, ListModelMixin):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer


class SpecialOfferViewSet(GenericViewSet, ListModelMixin):
    queryset = SpecialOffer.objects.all()
    serializer_class = SpecialOfferSerializer
