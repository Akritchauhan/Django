from django.shortcuts import render
from .models import UserProfile
from django.core.cache import cache

def users_list(request):
    users=cache.get('users_list')

    if not users:
        print("Cache miss")
        usres=UserProfile.objects.all()
        cache.set('users_list',users,timeout=30)
    else:
        print("Cache hit")
    
    return render(request,'users_list.html',{'users':users})