from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('clientes', ClientViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('clientes/<str:queryparams>', ClientViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('telefones', TelefoneViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('telefones/<str:id>', TelefoneViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('emails', EmailViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('emails/<str:id>', EmailViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
]