from rest_framework.routers import DefaultRouter
from api.v1.views.landing import (
    CertificateViewSet,
    FaqViewSet,
    PostViewSet,
    ResultViewSet,
    StarViewSet,
    BannerViewSet,
)

router = DefaultRouter()
router.register("landing/certificates", CertificateViewSet)
router.register("landing/faqs", FaqViewSet)
router.register("landing/posts", PostViewSet)
router.register("landing/results", ResultViewSet)
router.register("landing/stars", StarViewSet)
router.register("landing/banners", BannerViewSet)


urlpatterns = router.urls
