from django.urls import path

from .views import *

app_name = 'blog'

urlpatterns = [
    path('product/create', ProductCreateView.as_view()),
    path('product/delete/<str:pk>', ProductDeleteView.as_view()),
    path('product/update/<str:pk>', ProductUpdateView.as_view()),
    path('product/retrieve/<str:pk>', ProductRetrieveView.as_view()),
    path('product/name/<int:pk>', ProductNameUpdate.as_view()),
    # path('product/list/', ProductListView.as_view()),
    # path('review/create', ReviewCreateView.as_view()),
    # path('review/delete/<str:pk>', ReviewDeleteView.as_view()),
    # path('review/update/<str:pk>', ReviewUpdateView.as_view()),
    # path('review/retrieve/<str:pk>', ReviewRetrieveView.as_view()),
    # path('review/search/', BillingReviewView.as_view()),
    # path('review/list/', ReviewListView.as_view()),
    # path('basket/create', BasketCreateView.as_view()),
    # path('basket/delete/<str:pk>', BasketDeleteView.as_view()),
    # path('basket/update/<str:pk>', BasketUpdateView.as_view()),
    # path('basket/retrieve/<str:pk>', BasketRetrieveView.as_view()),
    # path('basket/search/', BillingBasketView.as_view()),
    # path('basket/list/', BasketListView.as_view()),
]
