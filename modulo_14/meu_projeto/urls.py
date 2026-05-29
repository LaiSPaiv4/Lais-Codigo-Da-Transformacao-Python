from django.contrib import admin
from django.urls import path
from cadastro_produtos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.listar_produtos, name='listar_produtos'),
    path('cadastrar/', views.cadastrar_produto, name='cadastrar_produto'),
    path('editar/<int:id>/', views.atualizar_produto, name='atualizar_produto'),
    path('excluir/<int:id>/', views.excluir_produto, name='excluir_produto'),
]