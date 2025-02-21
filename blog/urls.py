from django.urls import path

def get_urlpatterns():
    from . import views
    return [
        path('', views.inicio, name='inicio'),
        path('agregar-autor/', views.agregar_autor, name='agregar_autor'),
        path('agregar-categoria/', views.agregar_categoria, name='agregar_categoria'),
        path('agregar-post/', views.agregar_post, name='agregar_post'),
        path('buscar-post/', views.buscar_post, name='buscar_post'),
    ]

urlpatterns = get_urlpatterns()