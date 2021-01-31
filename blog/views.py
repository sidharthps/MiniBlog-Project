from django.shortcuts import render,HttpResponseRedirect

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
def signup(request):
    return render(request,'signup.html')

# Login Page
def user_login(request):
    return render(request,'login.html')
       


        

         
