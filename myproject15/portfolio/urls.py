from . import views
from django.urls import path

urlpatterns = [
    path('', views.student_list, name='student_list'),
]