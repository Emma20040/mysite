from django import forms
from .models import Question, Choice

class My_form(forms.ModelForm):
    class Meta:
        model=Choice
        fields = "__all__"
    
    