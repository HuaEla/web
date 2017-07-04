from django import forms
from .models import messageModel



class messageForm(forms.ModelForm):
    class Meta:
        model = messageModel
        fields=['name','email','text']