from django.urls import path

from .views import *

app_name = 'blog'

urlpatterns = [
    path('product/create', ProductCreateView.as_view()),
    path('review/create', ReviewCreateView.as_view()),
    path('basket/create', BasketCreateView.as_view()),
    #     path('product/delete/<int:product_id>', DeleteProductView.as_view())
    #     path('', views.index, name = 'index'),
    #     path('upload/', views.upload, name = 'upload-book'),
    #     path('update/<int:book_id>', views.update_book),
]
