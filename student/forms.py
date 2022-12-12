from django import forms
from django.contrib.auth.models import User
from django.db.models.constraints import UniqueConstraint
from . import models
from quiz import models as QMODEL
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
class StudentUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), validators=[validate_password])
    class Meta:
        model=User
        fields=['first_name','last_name','username','password','email']
        # widgets = {
        # 'password': forms.PasswordInput()
        # }
#     def clean_email(self): # Validates the email Field
#         email = self.cleaned_data.get('email')
#         if (email == ""):
#             print("error 1")
#             raise forms.ValidationError('This field cannot be left blank')
#         for instance in User.objects.all():
#             if instance.email == email:
#                 print(" Error 2")
#                 raise forms.ValidationError(email + ' is already present')
#         return email

class StudentForm(forms.ModelForm):
    class Meta:
        model=models.Student
        fields=['address','mobile','profile_pic']

