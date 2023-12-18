from django import forms
from django.forms import ModelForm

from .models import Task


class Taskform(forms.ModelForm):

    class Meta:
        model = Task
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(Taskform, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['placeholder'] = "Add new Task...."
        