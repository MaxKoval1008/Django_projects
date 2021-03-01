from django.urls import path

from .views import *

app_name = 'blog'

urlpatterns = [
    path('product/create', ProductCreateView.as_view()),
    path('product/delete/<str:pk>', ProductDeleteView.as_view()),
    path('product/update/<str:pk>', ProductUpdateView.as_view()),
    path('product/retrieve/<str:pk>', ProductRetrieveView.as_view()),
    path('product/search/', BillingProductView.as_view()),
    path('product/list/', ProductListView.as_view()),
    path('review/create', ReviewCreateView.as_view()),
    path('basket/create', BasketCreateView.as_view()),
]
