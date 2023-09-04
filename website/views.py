from django.shortcuts import render
from django.core.mail import send_mail 
from django.core.mail import EmailMessage
from dentist.settings import EMAIL_HOST_USER


# Create your views here

def home(request):
    return render(request,'home.html',{})


def contact(request):
    if request.method == "POST":
        message_name =  request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        # Send an email 

        send_mail(
            message_name,# subject 
            message, # message 
            message_email, # email 
            ['ondeyostephen0@gmail.com'], # To email 
        )
        return render(request,'contact.html',{'message_name':message_name})

    else:
        return render(request,'contact.html',{})
    
def about(request):
    return render(request,'about.html',{})

def service(request):
    return render(request,'service.html',{})


def pricing(request):
    return render(request,'pricing.html',{})


def appointment(request):
    if request.method == "POST":
        your_name =  request.POST['your-name']
        your_phone =  request.POST['your-phone']
        your_email =  request.POST['your-email']
        your_address =  request.POST['your-address']
        your_schedule =  request.POST['your-schedule']
        your_message =  request.POST['your-message']
        your_date =  request.POST['your-date']

        # Send an email
        #appointment = "Name: " + your_name + " Phone:" +  your_phone  + "Email:" + your_email +  "Address:" + your_address + "Schedule:" + your_schedule + "Day:" + your_date + "Message:" + your_message
        




        appointment =  "Name: " + your_name + "\n" + "Phone: " + your_phone + "\n" + "Email: " + your_email + "\n" + "Address: " + your_address + "\n" + "Schedule: " + your_schedule + "\n" + "Day: " + your_date + "\n" + "Message: " + your_message









        send_mail(
            'Appointment Request',# subject 
            appointment, # message 
            your_email, # email 
            ['stephenondeyo0@gmail.com'], # To email 
        )

        
        return render(request,'appointment.html',{'your_schedule':your_schedule,
                                                  'your_name':your_name,
                                                  'your_phone':your_phone,
                                                  'your_email':your_email,
                                                  'your_address':your_address,
                                                  'your_message':your_message,
                                                  'your_date':your_date})

    else:
        return render(request,'home.html',{})







