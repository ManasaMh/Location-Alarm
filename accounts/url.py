from django.urls import path
from .import views
from django.contrib.auth.views import login,logout

app_name='accounts'
urlpatterns=[
    
    path('login',login,{'template_name':'accounts/login.html'}),
    path('register',views.register),
    path('logout',logout,{'template_name':'accounts/logout.html'}),
]