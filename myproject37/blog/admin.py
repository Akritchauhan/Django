from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserLISTAdmin(admin.ModelAdmin):
    list_display=('name','sub')