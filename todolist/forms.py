from django import forms
from .models import TaskList

class TaskForm(forms.ModelForm):
    task = forms.CharField(label='', max_length=300)
    class Meta: 
        model = TaskList
        fields = ['task', 'done']