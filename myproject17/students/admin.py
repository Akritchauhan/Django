from django.contrib import admin

# Register your models here.
from students.models import Student
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=('name','age')
    search_fields=('name')
    list_filter=('age','city')
    ordering=('name',)