from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *
from django.contrib.auth.models import User

# Create your views here.

def login(request):
    return render(request, 'forms/login.html')

def sign_up(request):
    if request.method == 'POST':
        fullname = request.POST['fullname']
        m_no = request.POST['m_no']
        department = request.POST['department']
        jamb_no = request.POST['jamb_no']
        # date_now = request.POST['date_now']
        year_admitted = request.POST['year_admitted']
        phone_number = request.POST['phone_number']
        password = request.POST['password']
        comfirm_password = request.POST['comfirm_password']

        if StudentProfile.objects.filter(matric_no=m_no).exists():
            response_msg = 'Maric Number already exist!!'
            return JsonResponse({'success': False, 'message': response_msg})
        elif comfirm_password != password:
            response_msg = 'Password and comfirm password missed match'
            return JsonResponse({'success': False, 'message': response_msg})
        else:
            new_user = User.objects.create(username=m_no, password=password)
            new_user.save()
            get_user = User.objects.get(username=m_no)
            new_student = StudentProfile.objects.create(
                full_name=fullname.capitalize(), matric_no=m_no, department=department.capitalize(), jamb_no=jamb_no,
                year_addmitted=year_admitted, phone_number=phone_number, cleared=False, user=get_user
            )
            new_student.save()
            response_msg = 'Signup Completed Successful...'
            return JsonResponse({'success': True, 'message': response_msg})
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