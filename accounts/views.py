
from django.conf import settings
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.core.mail import send_mail
from accounts.forms import RegistrationForm
# Create your views here.
def register(request):
    
    if request.method=='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email=form.cleaned_data['email']
            name=form.cleaned_data['first_name']+" "+form.cleaned_data['last_name']
            subject="Welcome to location alarm"
            message="Thank you for registering "+name
            from_email=settings.EMAIL_HOST_USER
            #to_list=['tina.singasani@gmail.com']
            to_list=[email]
            send_mail(subject,message,from_email,to_list,fail_silently=False)
            
            return redirect('./login')
      
    else:

        form=RegistrationForm()
        return render(request,'accounts/signup.html',{'form':form})
   

def login(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            return render(request,'accounts/mapping.html')
             #return HttpResponse("logged in")
            #return redirect('./mapping')

    else:
        form=AuthenticationForm()
    return render(request,'accounts/login.html',{'form':form})    

def alarm(request):
    if request.method=='GET':
        print("Within alarm function")
        return render(request,'accounts/alarm.html')

def maps(request):
    return render(request,'accounts/mapping.html')
