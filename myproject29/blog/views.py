from django.shortcuts import render
from django.http import HttpResponse

def set_session(request):
    request.session['name'] = 'Akki'
    request.session['course'] = 'Django Framework'
    return HttpResponse("Session data set")

def get_session(request):
    name = request.session.get('name', 'Guest')
    course = request.session.get('course', 'Not enrolled')
    return HttpResponse(f"Welcome: {name}, you are learning: {course}")

def delete_session(request):
    # try:
    #     del request.session['name']
    #     del request.session['course']
    #     return HttpResponse("Session data deleted")
    # except KeyError:
    #     return HttpResponse("Session data not found to delete")
    request.session.flush()  # This will delete all session data
    return HttpResponse("All session data deleted")