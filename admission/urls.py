from django.urls import path
from .import views


urlpatterns=[
    path('', views.admission_list, name ='admission_list'),
    path('<int:pk>/', views.admission_detail, name ='admission_detail'),
    path('add/', views.admission_add, name = 'admission_add'),
]