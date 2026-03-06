from django.shortcuts import redirect, render

# Create your views here.
from django.http import HttpResponse
from .models import contact

def contact_form(request):
    return render(request, 'contact_form.html')

def submit_contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')

        if name and message:
            contact.objects.create(name=name, message=message)
            return HttpResponse(f"Thank you {name} for your message!")
        else:
            return HttpResponse("Please provide both name and message.")
    
    return redirect('contact_form')
        
    