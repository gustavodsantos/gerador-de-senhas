from django.urls import path

from mysite.base import views

app_name = 'base'

urlpatterns = [
    path('', views.gerador_senha, name='gerador_senha'),  # Página principal
]
