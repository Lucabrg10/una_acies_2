from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
    # Clienti - solo visualizzazione
    path('clienti/', views.clienti_list, name='clienti_list'),
    
    # Utenze - CRUD completo
    path('utenze/', views.utenze_list, name='utenze_list'),
    path('utenze/new/', views.utenza_create, name='utenza_create'),
    path('utenze/<int:pk>/edit/', views.utenza_update, name='utenza_update'),
    path('utenze/<int:pk>/delete/', views.utenza_delete, name='utenza_delete'),
    path('utenze/<int:pk>/letture/', views.utenza_letture, name='utenza_letture'),
    
    # Fatture - solo visualizzazione
    path('fatture/', views.fatture_list, name='fatture_list'),
    path('fatture/<int:pk>/letture/', views.fattura_letture, name='fattura_letture'),
    
    # Letture - solo creazione dall'utenza
    path('letture/new/', views.lettura_create, name='lettura_create'),
]