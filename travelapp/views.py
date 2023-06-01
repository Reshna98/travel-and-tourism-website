from django.shortcuts import render

def home(request):
    return render(request,'home.html')
def login(request):
    return render(request,'login.html')
def signup(request):
    return render(request,'signup.html')
def turkey(request):
    return render(request,'turkey.html')
def book(request):
    return render(request,'booknow.html')

def booknow(request):
    return render(request,'book.html')