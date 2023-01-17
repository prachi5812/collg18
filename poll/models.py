from django.db import models

GENDER=[
   ( "Male","Male"),
   ("Female",'Female'),
   ( "Others",'Others'),
]

COLORS=[
    ('',"--select--"),
    ('R',"RED"),
    ('G',"GREEN"),
    ('BL',"BLUE"),
    ('B',"BLACK"),
    ('W',"WHITE"),
]

# Create your models here.
class student_register(models.Model):
    fname=models.CharField(max_length=30,blank=True,verbose_name='First Name',help_text="first Name")
    lname=models.CharField(max_length=30,verbose_name="Last Name",help_text="Last Name")
    email=models.EmailField(help_text="Email Address")
    password1=models.CharField(max_length=10)
    password2=models.CharField(max_length=10)
    gender=models.CharField(max_length=10,choices=GENDER)
    colors=models.CharField(max_length=20,choices=COLORS)