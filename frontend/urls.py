from django.urls import path
from . import views

app_name = 'frontend'
urlpatterns = [
    path('', views.homePage, name='home'),
    path('products/', views.Product, name='products'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('delete-from-cart/<int:product_id>/', views.delete_from_cart, name='delete_from_cart'),
    path('purchase/', views.purchase_view, name='purchase'),
    path('cart/', views.cart_view, name='cart'),
    path('login/', views.login_request, name='login'),
    path('signup/', views.register_request, name='signup'),
    path('logout/', views.logout_request, name='logout'),
]
