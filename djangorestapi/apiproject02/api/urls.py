from . import views
from django.urls import path

urlpatterns = [
    path('students/',views.student_list,name='student_list')
]
