from django import forms
from .models import Task

class DatePickerInput(forms.DateInput):
    input_type = 'date'

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_number', 'task_name', 'task_description', 'task_category', 'task_status', 'task_created_date','task_due_date', 'task_completed_date', 'task_comment']
        labels ={
            'task_number': 'Task number', 
            'task_name': 'Task name', 
            'task_description': 'Description', 
            'task_category': 'Category', 
            'task_status': 'Status', 
            'task_created_date': 'Created date',
            'task_due_date': 'Due date', 
            'task_completed_date': 'Completed date', 
            'task_comment': 'Comment'
        }

        widgets = {
            'task_number': forms.NumberInput(attrs={'class': 'form-control'}), 
            'task_name': forms.TextInput(attrs={'class': 'form-control'}), 
            'task_description': forms.TextInput(attrs={'class': 'form-control'}), 
            'task_category': forms.TextInput(attrs={'class': 'form-control'}), 
            'task_status': forms.TextInput(attrs={'class': 'form-control'}), 
            'task_created_date': DatePickerInput(attrs={'class': 'form-control'}),
            'task_due_date': DatePickerInput(attrs={'class': 'form-control'}), 
            'task_completed_date': DatePickerInput(attrs={'class': 'form-control'}), 
            'task_comment': forms.TextInput(attrs={'class': 'form-control'})
        }