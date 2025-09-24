from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index_page, name="home"),
    path('select-user', views.selectUser_page, name="selectuser"),
    path('farmer-registration', views.farmerRegistration, name="farmerregistration"),
    path('user-registration', views.userRegistration, name="user-registration"),
    path('register', views.createUser, name="register"),
    path('login', views.login_page, name="login"),
    path('logout', views.userLogout, name="logout"),
    path('loginvalidation', views.login_validation, name="loginvalidate"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('farmer/add-product', views.addProduct, name="addProduct"),
    path('farmer/edit-product/<int:id>', views.editProduct, name="editProduct"),
    path('farmer/products', views.viewProducts, name="viewProducts"),
    path('api/product/add', views.addProductAPI, name="addProduct-api"),
    path('api/product/edit/<int:id>', views.editProductAPI, name="editProduct-api"),
    path('api/product/delete/<int:id>', views.deleteProductAPI, name="deleteProduct-api"),
]
