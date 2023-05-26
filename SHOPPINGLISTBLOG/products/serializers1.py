from django.contrib.auth.models import User
from django.utils.timezone import now
from .models import Produits, Category
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['pk', 'name']
        

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True)
    

    class Meta:
        model = Produits
        fields = ['pk', 'name', 'category']



class UserSerializer(serializers.ModelSerializer):
    days_since_joined = serializers.SerializerMethodField()

    class Meta:
        model = User

    def get_days_since_joined(self, obj):
        return (now() - obj.date_joined).days
      