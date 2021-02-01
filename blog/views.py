from django.shortcuts import render,HttpResponseRedirect
from .forms import SignUpForm,LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from . models import Post

# Home Page
def home(request):
    posts = Post.objects.all()
    return render(request,'home.html',{'posts':posts})

# About Page
def about(request):
    return render(request,'about.html')


# Contact Page
def contact(request):
    return render(request,'contact.html')


# DashBoard Page
def dashboard(request):
    posts = Post.objects.all()
    if request.user.is_authenticated:
        return render(request,'dashboard.html',{'posts':posts})
    else:
        return HttpResponseRedirect('/login/')
    

# Logout Page
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

# Signup Page
def user_signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request,'Congradulations!! You Are Become An Author ')
            form.save()
    else:
        form = SignUpForm()
    return render(request,'signup.html',{'form':form})

    

# Login Page
def user_login(request):
    if not request.user.is_authenticated:
      if request.method == "POST":
        form = LoginForm(request=request,data=request.POST)
        if form.is_valid():
            uname = form.cleaned_data['username']
            upass = form.cleaned_data['password']
            user = authenticate(username=uname,password=upass)
            if user is not None:
                login(request,user)
                messages.success(request,'Login Seccessfully!!')
                return HttpResponseRedirect('/dashboard/')
      else:
            form = LoginForm
            return render(request,'login.html',{'form':form})
    else:
        return HttpResponseRedirect('/dashboard/')

        
        

    

    
       


        

         
