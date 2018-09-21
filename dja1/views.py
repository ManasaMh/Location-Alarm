
from django.http import HttpResponse
from django.shortcuts import render,redirect
# Create your views here.
def loginredirect(request):
    return redirect('signup/login')
 