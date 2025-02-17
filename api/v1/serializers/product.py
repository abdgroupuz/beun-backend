from django.db.models import Min, Max

from rest_framework import serializers
from apps.product.models import Product, Category, Image, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    childrens = serializers.SerializerMethodField()

    def get_childrens(self, obj):
        if obj.childrens.exists():
            return CategorySerializer(obj.childrens.all(), many=True).data
        return []
    
    class Meta:
        model = Category
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    tags_ids = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Tag.objects.all(), write_only=True
    )
    images = ImageSerializer(many=True, read_only=True)
    images_ids = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Image.objects.all(), write_only=True
    )
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), write_only=True
    )

    class Meta:
        model = Product
        fields = "__all__"
        read_only_fields = ("hit_count", "sold_count", "created_at", "updated_at")
        extra_kwargs = {
            "tags_ids": {"write_only": True},
            "images_ids": {"write_only": True},
            "category_id": {"write_only": True},
        }
