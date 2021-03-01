from rest_framework import serializers
from .models import Product, Review, Basket


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'code', 'prise', 'amount', 'options')


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('username', 'comment')


class BasketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        fields = ('name', 'address', 'purchases')
