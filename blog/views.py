from django.shortcuts import render,HttpResponseRedirect
from .forms import SignUpForm,LoginForm,PostForm
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
#Add Post        

def add_post(request):
    if request.user.is_authenticated:
        if request.user.is_authenticated:
            if request.method == 'POST':
             form = PostForm(request.POST)
             if form.is_valid():
                title = form.cleaned_data['title']
                desc = form.cleaned_data['desc']
                pst = Post(title=title,desc=desc)
                pst.save()
                form = PostForm()
            else:
                form = PostForm()
            return render(request,'addpost.html',{'form':form})
            
            
    else:
        return HttpResponseRedirect('/login')        
                
           
    

              

#Update/Edit Post        

def update_post(request,id):
    form = PostForm
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Post.objects.get(pk=id)
            form = PostForm(request.POST,instance=pi)
            if form.is_valid():
                form.save()
            else:
                pi = Post.objects.get(pk=id)
                form = PostForm(instance=pi)    
        return render(request,'updatepost.html',{'form':form})
    else:
        return HttpResponseRedirect('/login')  

#Delete Post        

def delete_post(request,id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Post.objects.get(pk=id)
            pi.delete()
            return HttpResponseRedirect('/dashboard')
            
        
    else:
        return HttpResponseRedirect('/login')            


    

    
       


        

         
