from . import views
from django.urls import path

urlpatterns = [
    path('a/', views.blogs),
    path('form/', views.showforms),
    
]
