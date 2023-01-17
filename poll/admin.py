from django.contrib import admin
from .models import student_register

# Register your models here.
@admin.register(student_register)
class student_registerAdmin(admin.ModelAdmin):
    list_display=('id','fname','lname','email','password1','password2','gender','colors')
