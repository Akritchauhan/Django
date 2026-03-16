from . import views
from django.urls import path
urlpatterns = [
    path('set-cookies/',views.set_cookies,name='set-cookies'),
    path('get-cookies/',views.get_cookies,name='get-cookies'),
    path('delete-cookies/',views.delete_cookies,name='delete-cookies'),
]