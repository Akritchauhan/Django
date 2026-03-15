from . import views
from django.urls import path
urlpatterns = [
    path('set-session/',views.set_session,name='set_session'),
    path('get-session/',views.get_session,name='get_session'),
    path('delete-session/',views.delete_session,name='delete_session'),
]