from rest_framework import serializers
from .models import Product, Category, ProductField, Field
from api.v1.accounts.serializers import AuthorSerializer

# start category serializers
class CategoryAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        extra_kwargs = {
            'creator': {'read_only': True, 'required': False},
        }


class CategoryChildsChildrenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name')


class CategoryChildrenSerializer(serializers.ModelSerializer):
    children = CategoryChildsChildrenSerializer(many=True)
    class Meta:
        model = Category
        fields = ('name', 'children')


class CategoryClientSerializer(serializers.ModelSerializer):
    children = CategoryChildrenSerializer(many=True)
    class Meta:
        model = Category
        fields = ('name', 'image', 'children')
# end category serializers


# start Field serializers
class FieldAminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Field
        fields = '__all__'
        read_only_fields = ['creator', 'date_created']
        extra_kwargs = {
            'creator': {'required': False}
        }


class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Field
        fields = ['name', 'categories']
# end Field serializers


# start Product and ProductField  serializers
class ProductListSerializer(serializers.Serializer):
    class Meta:
        model = Product
        fields = (
            'title', 'image_main', 'price', 'price_is_dollar', 'region',
            'district', 'date_created'
        )


class ProductFieldSerializer(serializers.ModelSerializer):
    field = serializers.CharField(source="field.name", required=False)
    class Meta:
        model = ProductField
        exclude = ('product')


class ProductDetailSerializer(serializers.ModelSerializer):
    cat_fields = ProductFieldSerializer(many=True)
    author = AuthorSerializer()
    class Meta:
        model = Product
        exclude = (
            'auto_renewal', 'status', 'is_deleted', 'date_updated', 
        )


class ProductFieldCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductField
        exclude = ('product')


class ProductCreateSerializer(serializers.ModelSerializer):
    fields = ProductFieldSerializer(many=True)
    class Meta:
        model = Product
        exclude = (
            'views_count', 'status', 'is_deleted', 'date_created', 'date_updated', 
        )


class ProductRetrieveUpdateDestroySerializer(serializers.ModelSerializer):
    fields = ProductFieldSerializer(many=True)
    class Meta:
        model = Product
        exclude = (
            'number_id', 'is_deleted', 'views', 'date_created', 'date_updated', 
        )
# end Product and ProductField  serializers