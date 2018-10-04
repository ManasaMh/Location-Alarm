from django.urls import path
from .import views
from django.contrib.auth.views import login,logout

app_name='accounts'
urlpatterns=[
    
   #path('login',login,{'template_name':'accounts/login.html'}),
   path('login',views.login,name="login"),
    path('',views.register),
    path('accounts/alarm',views.alarm),
    #path('logout',logout,{'template_name':'accounts/logout.html'}),
    path('maps',views.maps)
]