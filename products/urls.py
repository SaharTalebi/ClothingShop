from django.urls import path

from . import views

urlpatterns=[
    path('', views.product_list_view, name='products'),
    path('<int:pk>', views.product_detail_view, name='product_detail'),
]