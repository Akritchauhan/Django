from django.urls import path
from .views import StudentListCreateAPI,StudentRetrieveUpdateDeleteAPI

urlpatterns = [
    path('students/',StudentListCreateAPI.as_view()),
    path('students/<int:pk>/',StudentRetrieveUpdateDeleteAPI.as_view()),
]
