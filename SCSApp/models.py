from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class StudentProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=20, blank=True)
    matric_no = models.CharField(max_length=100, blank=True)
    department = models.CharField(max_length=100, blank=True)
    jamb_no = models.CharField(max_length=100, blank=True)
    current_date = models.DateField(auto_now_add=True)
    year_addmitted = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=100, blank=True)
    cleared = models.BooleanField(True)

    def __str__(self):
        return self.matric_no

class Clearance(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    clearance_for = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.student

class Staff(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    role = models.EmailField(max_length=100, blank=True)

    def __str__(self):
        return self.email

