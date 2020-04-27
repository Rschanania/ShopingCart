from django.shortcuts import render

from django.http import HttpResponse
from django.core.mail import send_mail,send_mass_mail,mail_admins,mail_managers


def index(request):
    return render(request, 'index.html')

def send_mails(request):
    # mail1=send_mail( 'Subject here','Here is the message.','from@example.com',['to@example.com'],
    # fail_silently=False,html_message="<h1>Hello</h1>")
    # mail2=send_mail('Resume ','Here is the message','admin.admin.html',['the@gmail.com','themask@gmail.com'],fail_silently=False,html_message="<h1>Html messgae for the email</h1>")
    # if mail1 and mail2:
    #     return HttpResponse(mail1,mail2)
    # else:
    #     return Exception('Error')
    '''
    Sending mail using Send mass mail
    mail1=( 'Subject here','Here is the message.','from@example.com',['to@example.com'])
    mail2=('Resume ','Here is the message','admin.admin.html',['the@gmail.com','themask@gmail/.com'])
    mail=send_mass_mail((mail1,mail2,),fail_silently=False)
    if mail:
        return HttpResponse(mail)
    else:
        return Exception('Error')'''


def admin_mails(request):
    mail_admins('we found error','please fix the bugs ',fail_silently=False)
    mail_managers('we found error','please fix the bugs ',fail_silently=False)
    return HttpResponse('We send the email')
    