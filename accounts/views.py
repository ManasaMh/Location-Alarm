from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm

from accounts.forms import RegistrationForm
# Create your views here.
def register(request):
    
    if request.method=='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/account/login')
      
    else:

        form=RegistrationForm()
        return render(request,'accounts/signup.html',{'form':form})
   
