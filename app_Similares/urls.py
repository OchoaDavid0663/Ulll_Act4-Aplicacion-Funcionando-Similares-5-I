from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_similares, name='inicio_similares'),
    
    # URLs para Clientes
    path('clientes/', views.ver_clientes, name='ver_clientes'),
    path('clientes/agregar/', views.agregar_cliente, name='agregar_cliente'),
    path('clientes/actualizar/<int:pk>/', views.actualizar_cliente, name='actualizar_cliente'),
    path('clientes/realizar_actualizacion/<int:pk>/', views.realizar_actualizacion_cliente, name='realizar_actualizacion_cliente'),
    path('clientes/borrar/<int:pk>/', views.borrar_cliente, name='borrar_cliente'),

    # URLs para Medicamentos (NUEVAS)
    path('medicamentos/', views.ver_medicamentos, name='ver_medicamentos'),
    path('medicamentos/agregar/', views.agregar_medicamento, name='agregar_medicamento'),
    path('medicamentos/actualizar/<int:pk>/', views.actualizar_medicamento, name='actualizar_medicamento'),
    path('medicamentos/realizar_actualizacion/<int:pk>/', views.realizar_actualizacion_medicamento, name='realizar_actualizacion_medicamento'),
    path('medicamentos/borrar/<int:pk>/', views.borrar_medicamento, name='borrar_medicamento'),
]