from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def login(request):
    return render(request, 'forms/login.html')

def sign_up(request):
    return render(request, 'forms/sign-up.html')

def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

def user_management(request):
    return render(request, 'dashboard/user-management.html')

def student_management(request):
    return render(request, 'dashboard/student-management.html')

def student_record(request):
    return render(request, 'dashboard/student-record.html')