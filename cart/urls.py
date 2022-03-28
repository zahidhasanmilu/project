from django.urls import path
from .import views

urlpatterns = [
    path('user/<int:uid>/', views.cart, name='cart'),
    path('addTocart', views.addTocart, name='addTocart'),
]
