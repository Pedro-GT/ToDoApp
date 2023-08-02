from django import forms
from .models import Task

class DateInput(forms.DateInput):
    input_type = 'date'

class TaskForm(forms.ModelForm):
    
    name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Task Name", "class":"form-control"}), label="Task Name")
    dueDate = forms.DateTimeField(required=True, widget=DateInput(attrs={"placeholder":"DueDate", "class":"form-control"}), label="DueDate")
    priority = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"priority", "class":"form-control"}), label="priority")
    
    class Meta:
        model = Task    
        exclude = ('progress',)