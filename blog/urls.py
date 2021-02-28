from django.urls import path

from .views import *

app_name = 'blog'

urlpatterns = [
    path('product/create', ProductCreateView.as_view()),
    path('review/create', ReviewCreateView.as_view()),
    path('basket/create', BasketCreateView.as_view())
]
