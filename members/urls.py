from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.members_page),
    path('', views.index)
]