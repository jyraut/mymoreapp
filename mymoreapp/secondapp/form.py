from django import forms
from django import forms
from firstapp.models import *

#create form here
class student_form(forms.ModelForm):
    class Meta:
        model = student
        fields = '__all__'