

from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name = "Home"),

    path('about/',views.about, name = "about"),

    path('contact/',views.contact, name = "contact"),

    path('dashboard/',views.dashboard, name = "dashboard"),

    path('signup/',views.signup, name = "signup"),

    path('login/',views.user_login, name = "user_login"),
    
    path('logout/',views.user_logout, name = "user_logout"),
]
