from django import forms
from django.core import validators
from .models import student_register
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

# def color_starts_with(value):
#     if value[0]!='r':
#         raise forms.ValidationError("NAme should not be starts with r letter")
    
# class Registration(forms.Form):
#     fname=forms.CharField(label='First Name',validators=[validators.MinLengthValidator(4),validators.MaxLengthValidator(6)])
#     lname=forms.CharField(label='Last Name',validators=[validators.MinLengthValidator(5)])
#     email=forms.EmailField(label='Email')
#     password1=forms.CharField(label='Password1',validators=[validators.MinLengthValidator(6)])
#     password2=forms.CharField(label='Password2',validators=[validators.MinLengthValidator(6)])
#     gender=forms.CharField(widget=forms.RadioSelect(choices=GENDER))
#     colors=forms.CharField(widget=forms.SelectMultiple(choices=COLORS))

class Registration(forms.ModelForm):
    class Meta:
        model=student_register
        # fields="__all__"  
        fields=['fname','lname']
        # exclude=['lname']
        # labels={
        #     'fname':'User First name',
        #     'lname':'User Last Name',
        #     'email':'User Email Address',
        # }
        error_message={
            'fname':{'required':'User First Name is required'},
            'lname':{'required':'User Last Name is required'},
            'email':{'required':'User email is required'},
            'password1':{'required':'Password is must'},
            'password2':{'required':'Confirm password is also must'},
            

        }
        help_texts={
            'fname':'User First name',
            'lname':'User Last name',
            'email':'User Email Address',
        }
        widgets={
            'email':forms.EmailInput(),
            'password1':forms.PasswordInput(),
            'password2':forms.PasswordInput
        }



# cleaning specifie field
    # def clean_fname(self):
    #   val=self.cleaned_data['fname']
    #   if len(val)<4:
    #     raise forms.ValidationError('First anme should be grater than 4 characters')
    #   return val

    # def clean_lname(self):
    #   val=self.cleaned_data['lname']
    #   if len(val)<=6:
    #     raise forms.ValidationError('last anme should be grater or equal to 6 characters')
    #   elif len(val)>8:
    #     raise forms.ValidationError('last name should not be grater than 8 characters')
    #   return val

# def clean_email(self):
#     val=self.cleaned_data['lname']
#     if len(val)<=6:
#         raise forms.ValidationError('last anme should be grater or equal to 6 characters')
#     elif len(val)>8:
#         raise forms.ValidationError('last name should not be grater than 8 characters')
#     return val

#validation of complete django form at once
    # def clean(self):
    #   valname= super().clean()
    #   nm=self.cleaned_data['fname']
    #   if len(nm)<4:
    #     raise forms.ValidationError("Name shoulde be grater than 4 character")

    #   lnm=self.cleaned_data['lname']
    #   if len(lnm)<5:
    #     raise forms.ValidationError("Last name should be gratere than 5 characters")

# match two password fields
    # def clean(self):
    #    val=super().clean()
    #    pwd1=self.cleaned_data['password1']
    #    pwd2=self.cleaned_data['password2']

    #    if pwd1!=pwd2:
    #     raise forms.ValidationError("password does not match try another")

