from . import views
from django.urls import path

urlpatterns = [
    path('',views.student_create,name='student_create'),
    path('students/',views.student_list,name='student_list'),
    path('students/<int:pk>/',views.student_detail,name='student_detail'),
    path('students/<int:pk>/edit/',views.student_update,name='student_update'),
    path('students/<int:pk>/delete/',views.student_delete,name='student_delete'),
]