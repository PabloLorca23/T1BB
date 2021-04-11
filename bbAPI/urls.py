from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:serie>/<str:temporada>/', views.capitulo, name='capitulo'),
    path('<str:serie>/<str:temporada>/<int:episodio>', views.episodio, name='episodio'),
    path('<str:personaje>/', views.personaje, name='personaje')
    

    
]