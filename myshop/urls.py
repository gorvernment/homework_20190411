from django.urls import path
from . import views

app_name = 'myshop'

urlpatterns = [
    path('', views.item_list),
    path('items/<int:pk>/', views.item_detail),

]