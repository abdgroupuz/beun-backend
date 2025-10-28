from rest_framework.routers import DefaultRouter
from api.v1.views.landing import (
    CertificateViewSet,
    FaqViewSet,
    PostViewSet,
    ResultViewSet,
    StarViewSet,
    BannerViewSet,
    AwardViewSet,
    SpecialOfferViewSet
)

router = DefaultRouter()
router.register("landing/awards", AwardViewSet)
router.register("landing/certificates", CertificateViewSet)
router.register("landing/faqs", FaqViewSet)
router.register("landing/posts", PostViewSet)
router.register("landing/results", ResultViewSet)
router.register("landing/stars", StarViewSet)
router.register("landing/banners", BannerViewSet)
router.register("landing/special-offers", SpecialOfferViewSet, basename="special-offers")

urlpatterns = router.urls
