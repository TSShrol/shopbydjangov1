from django.contrib import admin
from django.urls import path

from . import views
app_name='shop'
urlpatterns = [
    path('product/<int:id>',views.product_detail, name='product_detail'),
    path('<slug:category_slug>/', views.product_list,name='product_list_by_category'),
    path('about_shop',views.about_shop,name='about_shop'),
    path('', views.product_list, name='product_list'),

]