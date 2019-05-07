from django.urls import path
from . import views

app_name = 'intro'

urlpatterns = [
    path('', views.info_list),
    path('infos/<int:pk>/', views.info_detail),
]