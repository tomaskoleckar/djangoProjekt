from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('kluby/', views.KlubListView.as_view(), name='topKluby'),
    path('kluby/<int:pk>/', views.KlubDetailView.as_view(), name='klub_detail'),
    path('kluby/souteze/<str:competition_name>/', views.KlubListView.as_view(), name='competition'),
]