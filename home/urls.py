from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('trending/', views.trending, name='trending'),
    path('search/', views.search, name='search'),
    path('product_details/<int:id>', views.details, name='product_details'),
    # path('productBycat/', views.productBycat, name='productBycat'),
]
