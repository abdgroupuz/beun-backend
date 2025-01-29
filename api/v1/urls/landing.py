from rest_framework.routers import DefaultRouter
from api.v1.views.landing import CertificateViewSet, FaqViewSet, PostViewSet, ResultViewSet, StarViewSet

router = DefaultRouter()
router.register("certificates", CertificateViewSet)
router.register("faqs", FaqViewSet)
router.register("posts", PostViewSet)
router.register("results", ResultViewSet)
router.register("stars", StarViewSet)


urlpatterns = router.urls
