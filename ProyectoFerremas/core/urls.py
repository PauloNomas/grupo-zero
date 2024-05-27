
# core/urls.py
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('login/', login, name="login"),
    path('producto/', producto, name="producto"),
    path('registro/', registro, name="registro"),
    path('tienda/', tienda, name="tienda"),
    path('cerrar_sesion/', cerrar_sesion, name="CERRAR_SESSION"),
    path('perfil/', perfil, name='perfil'),

    # Carrito
    path('carrito/', carrito, name="carrito"),
    
    # Metodos del Carrito
    path('agregar/<int:id_producto>/', agregar_al_carrito, name='AGREGAR_AL_CARRITO'),
    path('eliminar/<int:id_item>/', eliminar_del_carrito, name='ELIMINAR_DEL_CARRITO'),
    path('vaciar/', vaciar_carrito, name='VACIAR_CARRITO'),

    path('aumentar/<int:id_item>/', aumentar_cantidad, name='AUMENTAR_CANTIDAD'),
    path('disminuir/<int:id_item>/', disminuir_cantidad, name='DISMINUIR_CANTIDAD'),

    # Indicadores
    path('indicadores/', indicadores_view, name='indicadores'),

    # Búsqueda
    path('buscar/', buscar_productos, name='buscar_productos'),

    # Transbank
    path('create/', webpay_plus_create, name='webpay_plus_create'),
    path('commit/', webpay_plus_commit, name='webpay_plus_commit'),
    path('error/', webpay_plus_commit_error, name='webpay_plus_commit_error'),
    path('refund/', webpay_plus_refund, name='webpay_plus_refund'),
    path('refund-form/', webpay_plus_refund_form, name='webpay_plus_refund_form'),
    path('status-form/', show_create, name='webpay_plus_status_form'),
    path('status/', status, name='webpay_plus_status'),
    path('generar_boleta/', generar_boleta, name='generar_boleta'),

    path('api/', include('core.api_url')),  # Añadido
]