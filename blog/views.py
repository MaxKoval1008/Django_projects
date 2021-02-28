from rest_framework.generics import (
    CreateAPIView, RetrieveAPIView, ListAPIView, DestroyAPIView
)
from .models import Product, Review, Basket
from .serializers import ProductSerializer, ReviewSerializer, BasketSerializer


class ProductCreateView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class DeleteProductView(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ReviewCreateView(CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class BasketCreateView(CreateAPIView):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer
