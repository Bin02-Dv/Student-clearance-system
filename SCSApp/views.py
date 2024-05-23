from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User, auth
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

def logout(request):
    auth.logout(request)
    return redirect('/')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            response_msg = 'Login Successful....'
            return JsonResponse({'success': True, 'message': response_msg})
        else:
            response_msg = 'Invalid Login Credentials!!!'
            return JsonResponse({'success': False, 'message': response_msg})
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

        if User.objects.filter(username=m_no).exists():
            response_msg = 'Maric Number already exist!!'
            return JsonResponse({'success': False, 'message': response_msg})
        elif comfirm_password != password:
            response_msg = 'Password and comfirm password missed match'
            return JsonResponse({'success': False, 'message': response_msg})
        else:
            new_user = User.objects.create_user(username=m_no, password=password)
            new_user.save()
            get_user = User.objects.get(username=m_no)
            new_student = StudentProfile.objects.create(
                full_name=fullname.capitalize(), matric_no=m_no, department=department.capitalize(), jamb_no=jamb_no,
                year_addmitted=year_admitted, phone_number=phone_number, user=get_user
            )
            new_student.save()
            stu = StudentProfile.objects.get(matric_no=m_no)
            new_clearance_info = Clearance.objects.create(student=stu, clearance_for='Library', cleared=False)
            new_clearance_info = Clearance.objects.create(student=stu, clearance_for='H.O.D', cleared=False)
            new_clearance_info = Clearance.objects.create(student=stu, clearance_for='Hostel', cleared=False)
            new_clearance_info = Clearance.objects.create(student=stu, clearance_for='Bursary', cleared=False)
            new_clearance_info = Clearance.objects.create(student=stu, clearance_for='Registrer', cleared=False)
            new_clearance_info.save()
            response_msg = 'Signup Completed Successful...'
            return JsonResponse({'success': True, 'message': response_msg})
    return render(request, 'forms/sign-up.html')

@login_required(login_url='/')
def dashboard(request):
    current_user = User.objects.get(username=request.user)
    students = StudentProfile.objects.count()
    staffs = Staff.objects.count()
    context = {
        "user": current_user,
        "total_student": students,
        "total_staff": staffs,
    }
    return render(request, 'dashboard/dashboard.html', context)

@login_required(login_url='/')
def user_management(request):
    current_user = User.objects.get(username=request.user)
    context = {
        "user": current_user,
    }
    return render(request, 'dashboard/user-management.html', context)

@login_required(login_url='/')
def add_user(request):
    current_user = User.objects.get(username=request.user)
    context = {
        "user": current_user,
    }
    if request.method == 'POST':
        fullname = request.POST['fullname']
        email = request.POST['email']
        username = request.POST['username']
        role = request.POST['role']
        password = request.POST['password']
        comfirm_password = request.POST['comfirm_password']

        if User.objects.filter(email=email).exists():
            response_msg = 'Email already exist!!'
            return JsonResponse({'success': False, 'message': response_msg})
        elif User.objects.filter(username=username).exists():
            response_msg = 'Username already exist!!'
            return JsonResponse({'success': False, 'message': response_msg})
        elif comfirm_password != password:
            response_msg = 'Password and comfirm password missed match'
            return JsonResponse({'success': False, 'message': response_msg})
        else:
            new_user = User.objects.create_user(username=username, password=password, is_staff=True, email=email)
            new_user.save()
            get_user = User.objects.get(username=username)
            new_staff = Staff.objects.create(
                fullname=fullname.capitalize(), email=email, user=get_user,
                role=role
            )
            new_staff.save()
            response_msg = 'Staff Added Successful...'
            return JsonResponse({'success': True, 'message': response_msg})
    return render(request, 'dashboard/add-user.html', context)

@login_required(login_url='/')
def user_record(request):
    current_user = User.objects.get(username=request.user)
    staffs = Staff.objects.all().order_by('-id')
    context = {
        "user": current_user,
        "staffs": staffs,
    }
    return render(request, 'dashboard/user-record.html', context)

@login_required(login_url='/')
def student_management(request):
    current_user = User.objects.get(username=request.user)
    context = {
        "user": current_user,
    }
    return render(request, 'dashboard/student-management.html', context)

@login_required(login_url='/')
def student_record(request):
    students = StudentProfile.objects.all().order_by('-id')
    current_user = User.objects.get(username=request.user)
    context = {
        "user": current_user,
        "students": students,
    }
    return render(request, 'dashboard/student-record.html', context)

@login_required(login_url='/')
def cleared_student(request):
    current_user = User.objects.get(username=request.user)
    staff = Staff.objects.filter(user=current_user)
    staff_role = ''
    for role in staff:
        staff_role = role.role
    students = Clearance.objects.filter(cleared=True, clearance_for=staff_role)
    context = {
        "user": current_user,
        "students": students,
    }
    return render(request, 'dashboard/cleared-student.html', context)

@login_required(login_url='/')
def uncleared_student(request):
    current_user = User.objects.get(username=request.user)
    staff = Staff.objects.filter(user=current_user)
    staff_role = ''
    for role in staff:
        staff_role = role.role
    students = Clearance.objects.filter(cleared=False, clearance_for=staff_role)
    context = {
        "user": current_user,
        "students": students,
    }
    return render(request, 'dashboard/uncleared-student.html', context)

@login_required(login_url='/')
def clearance(request):
    current_user = User.objects.get(username=request.user)
    context = {
        "user": current_user,
    }
    return render(request, 'dashboard/clearance.html', context)

@login_required(login_url='/')
def student_clearance(request):
    current_user = User.objects.get(username=request.user)
    stu = StudentProfile.objects.get(user=current_user)
    stu_clearance = Clearance.objects.filter(student=stu)
    context = {
        "user": current_user,
        "clearance": stu_clearance,
    }
    return render(request, 'dashboard/student-clearance.html', context)

@login_required(login_url='/')
def change_password(request):
    current_user = User.objects.get(username=request.user)
    context = {
        "user": current_user,
    }
    return render(request, 'dashboard/change-password.html', context)

def stu_delete(request, id):
    student = User.objects.get(id=id)
    student.delete()
    response_msg = 'Student Deleted Successfully..'
    messages.success(request, response_msg)
    return redirect("student-record")

def clear_a_student(request, id):
    student = Clearance.objects.get(id=id)
    student.cleared = True
    student.save()
    response_msg = f'Student clearance for {student.clearance_for} is successful..'
    messages.success(request, response_msg)
    return redirect('uncleared-student')

def clearance_report(request):
    return render(request, 'clearance-report.html')