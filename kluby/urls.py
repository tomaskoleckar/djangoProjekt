from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('kluby/<int:pk>/', views.KlubDetailView.as_view(), name='klub_detail'),
]