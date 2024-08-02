from django.urls import path
from . import views
from django.contrib.auth import views as auth_view


urlpatterns = [
path('',views.Cart,name='cart'),
path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),

]