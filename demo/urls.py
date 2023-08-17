
from . import views
from django.urls import path

urlpatterns = [
    path('machine/', views.machine),
    path('', views.deep),
    path('review/', views.review, name='review'),
    path('news/', views.news , name='news'),
    path('nai/', views.nai, name='nai'),
    path('thr/', views.teacher_info, name='techer'),
    path('resister/', views.registration)
]
