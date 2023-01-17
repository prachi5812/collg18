from django.shortcuts import render,HttpResponseRedirect,redirect,HttpResponse
from .forms import Registration
from .models import student_register
# Create your views here.

def register(request):
  if request.method=="POST":
    fm=Registration(request.POST)
    if fm.is_valid():
         fname=fm.cleaned_data['fname']
         lname=fm.cleaned_data['lname']
         em=fm.cleaned_data['email']
         pwd1=fm.cleaned_data['password1']
         pwd2=fm.cleaned_data['password2']
         gen=fm.cleaned_data['gender']
         col=fm.cleaned_data['colors']
        #  fname=request.POST['fname']
        #  lname=request.POST['lname']
        #  em=request.POST['email']
        #  pwd1=request.POST['password1']
        #  gen=request.POST['gender']
        #  col=request.POST['colors']
        #  print("First Name\t",fname)
        #  print("Last Name\t",lname)
        #  print("Email\t",em)
        #  print("Password\t",pwd1)
        #  print("Gender\t",gen)
        #  print("colors\t",col)
        #  return HttpResponseRedirect("/")
        #  fm=Registration()
        #  return HttpResponse("form submitted successfully")
         data=student_register(fname=fname,lname=lname,email=em,password1=pwd1,password2=pwd2,gender=gen,colors=col)
         data.save()
         return HttpResponseRedirect('/thank/')
  else:
        fm=Registration()
  return render(request,'home.html',{'form':fm})

def thank(request):
    return render(request,'thanks.html')
