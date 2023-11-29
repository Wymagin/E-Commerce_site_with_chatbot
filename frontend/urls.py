
from django.urls import path
from . import views
from rest_framework import routers
from django.conf.urls import include

# router = routers.DefaultRouter()
# router.register('products', views.ProductView)
# router.register('users', views.UserView)


app_name = 'frontend'
urlpatterns = [
    path('', views.homePage, name='home'),
    path('products/', views.Product, name='products'),
    path('login/', views.login_request, name='login'),
    path('signup/', views.register_request, name='signup'),
    path('logout/', views.logout_request, name='logout'),
    # path("api/", include(router.urls)),
    path("api-auth/", include('rest_framework.urls', namespace='rest_framework')),
    path('products-set/', views.MyModelList.as_view()),

    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # path('<int:pk>/results/',views.ResultsView.as_view(), name='results'),
    # path('<int:question_id>/vote/',views.vote, name='vote'),
]
