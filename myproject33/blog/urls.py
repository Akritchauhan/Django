from . import views
from django.urls import path

urlpatterns =[
    path('bulk-email/',views.send_bulk_email, name='send_bulk-email'),
]