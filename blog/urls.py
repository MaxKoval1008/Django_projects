from django.urls import path

from .views import *

app_name = 'blog'

urlpatterns = [
    path('product/create', ProductCreateView.as_view())
]