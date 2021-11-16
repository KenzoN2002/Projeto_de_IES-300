from django.urls import path
from . import views

#Caminhos de path das urls

urlpatterns = [
     path('', views.index, name='index'),
     path('comandas/', views.ComandaListView.as_view(), name='Comandas'),
    path('comanda/<int:pk>',
         views.ComandaDetailView.as_view(), name='comanda-detail'),
    path('comanda/create/', views.ComandaCreate.as_view(), name='comanda-create'),
    path('comanda/<int:pk>/update/', views.ComandaUpdate.as_view(), name='comanda-update'),
    path('comanda/<int:pk>/delete/', views.ComandaDelete.as_view(), name='comanda-delete'),
]
