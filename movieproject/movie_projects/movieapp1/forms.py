from django import forms
from .models import Movielist

class MovieForm(forms.ModelForm):
    class Meta:
        model=Movielist
        fields=['name','desc','year','img']

