from django.urls import path
from . import views
from .views import product_dispaly

urlpatterns = [
    path('', views.product_dispaly, name='home'),
    path('product/<str:id>/', views.more_details, name="more_details"),
    path('about/', views.aboutPage, name="about"),
    path('orders/', views.orders, name="orders"),
    path('cancelOrder/<str:id>/', views.cancelOrder, name="cancelOrder"),
]
