from rest_framework.generics import (
    CreateAPIView, RetrieveAPIView, ListAPIView, DestroyAPIView
)
from .models import Product, Review, Basket
from .serializers import ProductSerializer, ReviewSerializer, BasketSerializer


class ProductCreateView(CreateAPIView, RetrieveAPIView, ListAPIView, DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ReviewCreateView(CreateAPIView, RetrieveAPIView, ListAPIView, DestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class BasketCreateView(CreateAPIView, RetrieveAPIView, ListAPIView, DestroyAPIView):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer
