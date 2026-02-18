from django.shortcuts import render
from datetime import datetime
# Create your views here.
def blog_list(request):
    blogs=[
        {'title':'My First Post',"is_featured":True,"author":"John Doe"},
        {'title':'My Second Post',"is_featured":False,"author":""},
        {'title':'My Third Post',"is_featured":False,"author":"Alice Smith"},
    ]
    context={
        "blogs":blogs,
        "today":datetime.now(),
        "html_code":"<h1>This is a heading</h1>",
    }
    return render(request, 'blog/home.html', context)