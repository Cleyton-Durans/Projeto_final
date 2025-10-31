from django.urls import path
from . import views

urlpatterns = [
    path('', views.fazer_reserva, name='fazer_reserva'),
    path('reservas/', views.lista_reservas, name='lista_reserva'),
    path('editar/<int:id>/', views.atualizar_reserva, name='editar_reserva'),
    path('deletar/<int:id>/', views.deletar_reserva, name='deletar_reserva'),
    path('status/<int:id>/<str:novo_status>/', views.alterar_status, name='alterar_status'),
    path('minhas_reservas/', views.minhas_reservas, name='minhas_reservas'),
    path('logout/', views.logout_view, name='logout'),  
    path('fazer_reserva_admin/', views.fazer_reserva_admin, name='fazer_reserva_admin'),
    
]

