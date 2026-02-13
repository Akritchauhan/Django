from django.http import HttpResponse

def post_details(request,post_id):
    return HttpResponse(f'This is the post details page for post ID: {post_id}')

def user_profile(request,username):
    return HttpResponse(f'This is the user profile page for username: {username}')

def archive(request,year):
    return HttpResponse(f'This is the archive page for year: {year}')
# def article_details(request,year,month):
#     return HttpResponse(f'This is the article details page for year: {year}, month: {month}')

def article_details(request,**kwargs):
    return HttpResponse(f'This is the article details page for year: {kwargs.get("year")}, month: {kwargs.get("month")}')