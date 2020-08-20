from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('<str:portfolio_item>/', views.portfolio_item, name='portfolio_item'),
]