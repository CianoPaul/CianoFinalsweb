from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard, name='item'),
    path('table/', views.table , name='table'),
    path('edit/<int:id>', views.edit, name='edit'),
]

