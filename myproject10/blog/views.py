from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'base.html')

def blog(request):
    student = [
        {'name': 'Alice', 'age': 20},
        {'name': 'Bob', 'age': 22},
    ]
    return render(request,'blog.html', {'students': student})