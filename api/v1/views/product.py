from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import SAFE_METHODS, IsAdminUser, AllowAny
from django_filters.rest_framework.backends import DjangoFilterBackend

from dj_rest_auth.jwt_auth import JWTCookieAuthentication

from apps.product.models import Category, Image, Product, Tag
from api.v1.serializers.product import CategorySerializer, ImageSerializer, ProductSerializer, TagSerializer
from api.v1.filters.product import ProductFilter

class TagViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer    
    authentication_classes = [JWTCookieAuthentication]
    
    def get_authenticators(self):
        if self.request.method in SAFE_METHODS:
            return []
        return super().get_authenticators()
    
    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return [AllowAny()]
        return [IsAdminUser()]


class ImageViewSet(ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    authentication_classes = [JWTCookieAuthentication]
    
    def get_authenticators(self):
        if self.request.method in SAFE_METHODS:
            return []
        return super().get_authenticators()

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return [AllowAny()]
        return [IsAdminUser()]


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.filter(parent=None)
    serializer_class = CategorySerializer
    authentication_classes = [JWTCookieAuthentication]
    
    def get_authenticators(self):
        if self.request.method in SAFE_METHODS:
            return []
        return super().get_authenticators()

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return [AllowAny()]
        return [IsAdminUser()]


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [JWTCookieAuthentication]
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ProductFilter
    
    def get_authenticators(self):
        if self.request.method in SAFE_METHODS:
            return []
        return super().get_authenticators()

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return [AllowAny()]
        return [IsAdminUser()]
