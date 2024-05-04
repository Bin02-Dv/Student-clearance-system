from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('sign-up/', views.sign_up, name='sign-up'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('user-management/', views.user_management, name='user-management'),
    path('student-management/', views.student_management, name='student-management'),
]
