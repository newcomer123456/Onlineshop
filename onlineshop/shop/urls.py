from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.product_list, name="products"),
    path('product/<int:id>', views.product_details, name="product-details"),
    path('register/', views.register_view, name="register"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('create-new-product/', views.product_creation, name="new-product"),
]
