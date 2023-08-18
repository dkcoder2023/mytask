from django.urls import path
from myapp import views

urlpatterns = [
    path('',views.Index,name="home"),
    path('contact/',views.Contact,name="contact"),
    path('about/',views.About,name="about"),
    path('login/',views.Login,name="login"),
    path('signup/',views.Signup,name="signup"),
    
]
