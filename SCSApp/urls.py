from django.urls import path
from . import views

urlpatterns = [
    path('logout/', views.logout, name='logout'),
    path('', views.login, name='login'),
    path('signup/', views.sign_up, name='signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('user-management/', views.user_management, name='user-management'),
    path('add-user/', views.add_user, name='add-user'),
    path('user-record/', views.user_record, name='user-record'),
    path('student-management/', views.student_management, name='student-management'),
    path('student-record/', views.student_record, name='student-record'),
    path('clearance/', views.clearance, name='clearance'),
    path('clear/<int:id>', views.clear_a_student, name='clear'),
    path('student-clearance/', views.student_clearance, name='student-clearance'),
    path('cleared-student/', views.cleared_student, name='cleared-student'),
    path('uncleared-student/', views.uncleared_student, name='uncleared-student'),
    path('change-password/', views.change_password, name='change-password'),
    path('clearance-report/', views.clearance_report, name='clearance-report'),

    # Delete section
    path('stu-delete/<int:id>', views.stu_delete, name='stu-delete'),
]
