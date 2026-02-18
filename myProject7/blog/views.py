from django.shortcuts import render
from datetime import datetime
# Create your views here.
def home(request):
    post={
        'title':'My First Post',
        'content':'This is the content of my first post.',
        'author':'John Doe',
        'price': 100,
        'published_date': datetime.now(),
        'number': 42,
        'tags': ['django', 'python', 'web development']
    }
    return render(request, 'blog/home.html', {'post': post})