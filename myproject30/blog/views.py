from django.shortcuts import render
from django.http import HttpResponse

def set_cookies(request):
    response = HttpResponse("Cookies Set SUCCESSFULLY")
    response.set_cookie('name','akki',max_age=60*60*24*7)
    response.set_cookie('course','django',max_age=60*60*24*7)
    return response

def get_cookies(request):
    name = request.COOKIES.get('name')
    course = request.COOKIES.get('course')
    return HttpResponse(f"Cookies Value: {name}, {course}")

def delete_cookies(request):
    response = HttpResponse("Cookies Deleted")
    response.delete_cookie('name')
    response.delete_cookie('course')
    return response


