from drf_spectacular.contrib.django_filters import DjangoFilterBackend
from rest_framework import generics
from rest_framework.generics import (
    CreateAPIView, RetrieveAPIView, ListAPIView, DestroyAPIView, UpdateAPIView, GenericAPIView
)
from .models import Product, Review, Basket
from .serializers import ProductSerializer, ProductNameSerializer  # , ReviewSerializer, BasketSerializer
from rest_framework.response import Response

"""Products"""


class ProductCreateView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDeleteView(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductUpdateView(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductRetrieveView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductNamePatchView(GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductNameSerializer

    def patch(self, request, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class BillingProductView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']


# """Review"""
#
#
# class ReviewCreateView(CreateAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
#
#
# class ReviewDeleteView(DestroyAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
#
#
# class ReviewUpdateView(UpdateAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
#
#
# class ReviewNamePatchView(GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewNameSerializer
#
#
# class ReviewRetrieveView(RetrieveAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
#
#
# class ReviewListView(ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#
#
# class BillingReviewView(ListAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['username']
#
#
# """Baskets"""
#
#
# class BasketCreateView(CreateAPIView):
#     queryset = Basket.objects.all()
#     serializer_class = BasketSerializer
#
#
# class BasketDeleteView(DestroyAPIView):
#     queryset = Basket.objects.all()
#     serializer_class = BasketSerializer
#
#
# class BasketUpdateView(UpdateAPIView):
#     queryset = Basket.objects.all()
#     serializer_class = BasketSerializer
#
#
# class BasketRetrieveView(RetrieveAPIView):
#     queryset = Basket.objects.all()
#     serializer_class = BasketSerializer
#
#
# class BasketListView(ListAPIView):
#     queryset = Basket.objects.all()
#     serializer_class = BasketSerializer
#
#
# class BillingBasketView(ListAPIView):
#     queryset = Basket.objects.all()
#     serializer_class = BasketSerializer
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['name']
