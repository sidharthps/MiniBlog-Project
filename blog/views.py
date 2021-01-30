from django.shortcuts import render

# Home Page
def home(request):
    return render(request,'home.html')

# About Page
def about(request):
    return render(request,'about.html')    

# Contact Page
def contact(request):
    return render(request,'contact.html')
    
         
