from django.urls import path
from carts import views
from carts.views import cart_add, cart_change, cart_remove
app_name = 'carts'

urlpatterns = [
    path('cart_add/<str:product_slug>/', views.cart_add, name='cart_add'),    
    path('cart_change/<str:product_slug>/', views.cart_change, name='cart_change'),
    path('cart_remove/<int:cart_id>/', views.cart_remove, name='cart_remove'),
    
]