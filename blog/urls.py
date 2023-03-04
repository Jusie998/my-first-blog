from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('route2/', views.route_two, name='route_two')
]