from . import views
from django.urls import path

urlpatterns = [
    path('', views.deep_learning, name='deep'),
    path('sub/',views.sub ),
    path('class/', views.sub_line.as_view()),
]
