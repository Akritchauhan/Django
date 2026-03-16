
from django.core.mail import send_mail,EmailMessage
from django.template.loader import render_to_string
from django.http import HttpResponse

# def send_email(request):
#    subject = 'Hello from Django'
#    message = 'This is a test email sent from a Django view.'    
#    from_email = 'chauhanakrit516gmail.com'
#    recipient_list = ['akritchauhan.work@gmail.com']
#    send_mail(subject,message, from_email, recipient_list)
#    return HttpResponse('Email sent successfully!')

def send_email(request):
    subject = 'Hello from Django'
    message = render_to_string('email_template.html', {'name': 'Akrit'})
    email = EmailMessage(subject, message, to=['23206@iiitu.ac.in'])
    email.content_subtype = 'html'  # Set the content type to HTML
    email.send()
    return HttpResponse('Email sent successfully!')