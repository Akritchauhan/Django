from django.shortcuts import render
from datetime import datetime
# Create your views here.
class user:
    def __init__(self,name,age):
        self.name=name
        self.age=age
def home(request):
    context={
        'name':'Akrit',
        'age':20,
        'skill':["python",'verilog','sv'],
        "user":user('Akki',21),
        "blog":{'title':'My first blog',
                'content':'<b>This is my first blog content</b>',
                'created_at':datetime(2026,8,18,10,30),
                },
                "empty_value":None,
    }
    return render(request,'home.html',context)