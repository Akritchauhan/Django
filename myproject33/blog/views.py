from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponse
from django.template.loader import render_to_string

# def send_bulk_email(request):
#     messages1 =('welcome User1','hello user1,welcome!','chauhanakrit516@gmail.com',['23206@iiitu.ac.in'])

#     messages2=('welcome User2','hello user2,welcome!','chauhanakrit516@gmail.com',['akritchauhan.work@gmail.com'])


#     send_mass_mail((messages1,messages2),fail_silently=False)

#     return HttpResponse("bulk email sent!")
def send_bulk_email(request):
    subject="welcome"
    from_email="chauhanakrit516@gmail.com"
    recipient_list=['23206@iiitu.ac.in','akritchauhan.work@gmail.com']

    html_content =render_to_string("welcome_email.html",{'username':'Akki'})

    msg=EmailMultiAlternatives(subject,'hello',from_email,recipient_list)
    msg.attach_alternative(html_content,"text/html")
    # msg.attach_file()
    msg.send()

    return HttpResponse("sent!")