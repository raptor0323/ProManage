from django.urls import path
from . import views


urlpatterns = [
    path('',views.leads_list, name = 'leads_list'),
    path('<int:pk>/', views.leads_detail, name='leads_detail'),
    path('<int:pk>/delete/', views.leads_delete, name='leads_delete'),
    path('<int:pk>/edit/', views.leads_edit, name='leads_edit'),
    path('<int:pk>/convert/', views.convert_to_admission, name='leads_convert'),
    path('add_lead/', views.add_lead, name = 'add_lead'),
    
]