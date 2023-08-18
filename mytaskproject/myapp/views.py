from django.shortcuts import render

def Index(request):
    return render(request,'index.html')

def Contact(request):
    return render(request,'contact.html')

def About(request):
    return render(request,'about.html')


def Login(request):
    return render(request,'Login.html')

def Signup(request):
    return render(request,'Signup.html')