from django.contrib import admin

# Register your models here.
from portfolio.models import Student
admin.site.register(Student)
from portfolio.models import Profile
admin.site.register(Profile)