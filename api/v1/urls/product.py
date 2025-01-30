from rest_framework.routers import DefaultRouter
from api.v1.views.product import CategoryViewSet, ImageViewSet, ProductViewSet, TagViewSet

router = DefaultRouter()
router.register("product/categories", CategoryViewSet)
router.register("product/images", ImageViewSet)
router.register("product/products", ProductViewSet)
router.register("product/tags", TagViewSet)

urlpatterns = router.urls
