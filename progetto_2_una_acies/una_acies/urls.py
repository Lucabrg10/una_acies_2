from django.urls import path
from . import views

urlpatterns = [
    path('', views.utenze_list, name='utenze_list'),
    path('utenze/', views.utenze_list, name='utenze_list'),
    path('utenze/aggiungi/', views.utenza_create, name='utenza_create'),
    path('utenze/<int:pk>/modifica/', views.utenza_update, name='utenza_update'),
    path('utenze/<int:pk>/elimina/', views.utenza_delete, name='utenza_delete'),
    path('clienti/', views.clienti_list, name='clienti_list'),
    path('fatture/', views.fatture_list, name='fatture_list'),
]

