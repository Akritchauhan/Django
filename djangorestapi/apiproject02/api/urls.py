from . import views
from django.urls import path

urlpatterns = [
    path('students/',views.student_list,name='student_list'),
    path('add/',views.add_studentlist,name='add_studentlist'),
    path('update/<int:pk>',views.update_student,name='update_student'),
    path('delete/<int:pk>',views.delete_student,name='delete_student')
]
