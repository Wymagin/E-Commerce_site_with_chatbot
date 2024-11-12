from django.urls import path
from . import views

app_name = 'frontend'
urlpatterns = [
    path('', views.homePage, name='home'),
    path('products/', views.Product, name='products'),
    path('login/', views.login_request, name='login'),
    path('signup/', views.register_request, name='signup'),
    path('logout/', views.logout_request, name='logout'),
]
