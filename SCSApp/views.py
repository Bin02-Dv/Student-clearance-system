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

def add_user(request):
    return render(request, 'dashboard/add-user.html')

def user_record(request):
    return render(request, 'dashboard/user-record.html')

def student_management(request):
    return render(request, 'dashboard/student-management.html')

def student_record(request):
    return render(request, 'dashboard/student-record.html')

def cleared_student(request):
    return render(request, 'dashboard/cleared-student.html')

def uncleared_student(request):
    return render(request, 'dashboard/uncleared-student.html')

def clearance(request):
    return render(request, 'dashboard/clearance.html')

def student_clearance(request):
    return render(request, 'dashboard/student-clearance.html')

def change_password(request):
    return render(request, 'dashboard/change-password.html')