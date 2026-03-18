from django.shortcuts import render
from .models import YoutubeUser
from django.core.cache import cache

def users_list(request):
    users=cache.get('users_data')
    if not users:
       print("cache miss")
       users=YoutubeUser.objects.all()
       cache.set('users_data',users,timeout=60) #for 60s
    else:
        print("cache hit")
    return render(request,'users_list.html',{'users': users})


 