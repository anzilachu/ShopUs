from django.urls import path
from . import views
app_name='cart'

urlpatterns = [
    path('shop/',views.cart_detail,name='cart_detail'),
    path('shop/add/<int:product_id>/',views.add_cart,name='add_cart'),
    path('shop/remove/<int:product_id>/',views.cart_remove,name='cart_remove'),
    path('shop/full_remove/<int:product_id>/',views.full_remove,name='full_remove'),
]
