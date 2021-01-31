from django.shortcuts import render,HttpResponseRedirect
from .forms import SignUpForm,LoginForm

# Home Page
def home(request):
    return render(request,'home.html')

# About Page
def about(request):
    return render(request,'about.html')


# Contact Page
def contact(request):
    return render(request,'contact.html')


# DashBoard Page
def dashboard(request):
    return render(request,'dashboard.html')

# Logout Page
def user_logout(request):
    return HttpResponseRedirect('/')

# Signup Page
def user_signup(request):
    form = SignUpForm()
    return render(request,'signup.html',{'form':form})

# Login Page
def user_login(request):
    form = LoginForm
    return render(request,'login.html',{'form':form})

    
       


        

         
