from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from templated_email import send_templated_mail

# Create your views here.
def home(request):
    return render(request,'home.html',{})    

def contact(request):
    if request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        service = request.POST.get('select')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        send_templated_mail(
                template_name='welcome',
                from_email=email,
                recipient_list=['papadiawara@hotmail.fr','contact@iaas-senegal.com'],
                context={
                    'firstname':firstname,
                    'lastname':lastname,
                    'email':email,
                    'subject':subject,
                    'service':service,
                    'message':message,
                    'phone':phone,
                },
        )
        return render(request,'contact.html',{'firstname':firstname,'lastname':lastname,'message':message,'email':email,'phone':phone,'service':service,'subject':subject})    
    else:    
        return render(request,'contact.html',{})    