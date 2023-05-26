from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_flex_fields import FlexFieldsModelSerializer
from django.contrib.auth.models import User
from django.utils.timezone import now
from rest_framework import serializers
from .models import Produits,CustomerReportRecord,Category,Comment
from rest_framework.reverse import reverse





class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ['pk', 'name']
        expandable_fields = {
          'products': ('products.ProductsListSerializer', {'many': True})
        }


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["title","content","product","user","created",""]


class ProductsListSerializer(serializers.ModelSerializer):
    absolute_url=serializers.SerializerMethodField()
    category = CategorySerializer(many=True)
    

    class Meta:
        model=Produits
        fields=["id",
            "nom","category",
                "description",
                "image","note",
                "absolute_url",
                "category"
                ]
        expandable_fields = {
          'category': (CategorySerializer, {'many': True}),
          'comments': (CommentSerializer, {'many': True}),}
        


    def get_absolute_url(self,obj):
        return reverse('products_list')


class ProductsDetailSerializer(serializers.ModelSerializer):
    update = serializers.SerializerMethodField()
    delete=serializers.SerializerMethodField()
    category = CategorySerializer(many=True)
    class Meta:
        model=Produits
        fields=["id",
            "nom",
                "description","category",
                "image","note"
                ,"update",
                "delete",
                "category"
                 ]
        expandable_fields = {
          'category': (CategorySerializer, {'many': True}),
            'comments': (CommentSerializer, {'many': True}),
        }
    def get_update(sel,obj):

        return reverse('products_update',args=(obj.pk,))
    
    def get_delete(self,obj):

        return reverse('products_delete',args=(obj.pk,))
    def get_absolute_url(self,obj):
        return reverse('products_detail')

class UserSerializer(serializers.ModelSerializer):
    days_since_joined = serializers.SerializerMethodField()

    class Meta:
        model = User

    def get_days_since_joined(self, obj):
        return (now() - obj.date_joined).days
    
class CommentSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Comment
        fields = ['pk', 'title', 'content', 'created', 'updated']
        expandable_fields = {
            'product': CategorySerializer,
            'user': UserSerializer
        }




class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['username'] = user.username
        return token