from django import forms
from django.forms import widgets

from myapp.models import Comic

class CreateComicForm(forms.ModelForm):
    
    # create meta class
    class Meta:
        # specify model to be used
        model = Comic
        
        # specify fields to be used
        fields = [
            "name" ,
            "genre"
        ]