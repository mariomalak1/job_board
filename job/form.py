from django import forms
from django.forms import fields
from .models import Apply
#create your form

class Applyform(forms.ModelForm):
    class Meta:
        model = Apply
        fields = ['name' , 'email' , 'website' , 'cv' , 'cover_leter' ]