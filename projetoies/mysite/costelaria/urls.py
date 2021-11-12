from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pratos/', views.PratoListView.as_view(), name='pratos'),
    path('prato/<int:pk>',
         views.PratoDetailView.as_view(), name='prato-detail'),
    path('prato/create/', views.PratoCreate.as_view(), name='prato-create'),
    path('prato/<int:pk>/update/', views.PratoUpdate.as_view(), name='prato-update'),
    path('prato/<int:pk>/delete/', views.PratoDelete.as_view(), name='prato-delete'),
    path('sobremesas/', views.SobremesaListView.as_view(), name='sobremesas'),
    path('sobremesa/<int:pk>',
         views.SobremesaDetailView.as_view(), name='sobremesa-detail'),
    path('sobremesa/create/', views.SobremesaCreate.as_view(), name='sobremesa-create'),
    path('sobremesa/<int:pk>/update/', views.SobremesaUpdate.as_view(), name='sobremesa-update'),
    path('sobremesa/<int:pk>/delete/', views.SobremesaDelete.as_view(), name='sobremesa-delete'),
     path('bebidas/', views.BebidaListView.as_view(), name='Bebidas'),
    path('bebida/<int:pk>',
         views.BebidaDetailView.as_view(), name='bebida-detail'),
    path('bebida/create/', views.BebidaCreate.as_view(), name='bebida-create'),
    path('bebida/<int:pk>/update/', views.BebidaUpdate.as_view(), name='bebida-update'),
    path('bebida/<int:pk>/delete/', views.BebidaDelete.as_view(), name='bebida-delete'),
]

urlpatterns += [
     path('comandas/', views.ComandaListView.as_view(), name='Comandas'),
    path('comanda/<int:pk>',
         views.ComandaDetailView.as_view(), name='comanda-detail'),
    path('comanda/create/', views.ComandaCreate.as_view(), name='comanda-create'),
    path('comanda/<int:pk>/update/', views.ComandaUpdate.as_view(), name='comanda-update'),
    path('comanda/<int:pk>/delete/', views.ComandaDelete.as_view(), name='comanda-delete'),
]
