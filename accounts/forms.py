from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    email=forms.EmailField(required=True)
    class Meta:
        model =User
        fields=('username',
        'first_name',
        'last_name',
        'email',
        'password1',
        'password2')
        def save(self, commit=True):

            user=super(RegistrationForm,self).save(commit=False)
            user.email = form.cleaned_data["email"]
            user.first_name=form.cleaned_data['first_name']
            user.last_name=form.cleaned_data['last_name']
           # password1 = form.cleaned_data.get('password1')
            #password2 = form.cleaned_data.get('password2')
            #if password1!= password2:
             #    raise forms.ValidationError(
             #   "password and confirm_password does not match")
            
            if commit:
                user.save()
            return user
           
