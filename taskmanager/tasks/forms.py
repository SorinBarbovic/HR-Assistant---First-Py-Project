from django import forms
from .models import Holiday, Shopping, Task

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

class HolidayForm(forms.ModelForm):
    class Meta:
        model = Holiday
        fields = ['holiday_number', 'holiday_type', 'holiday_description', 'holiday_from', 'holiday_to', 'holiday_status', 'holiday_start_date','holiday_end_date', 'holiday_budget', 'holiday_comment']
        labels ={
            'holiday_number': 'Holiday number', 
            'holiday_type': 'Holiday name', 
            'holiday_description': 'Description', 
            'holiday_from': 'From', 
            'holiday_to': 'To', 
            'holiday_status': 'Status', 
            'holiday_start_date': 'Start date',
            'holiday_end_date': 'End date', 
            'holiday_budget': 'Budget', 
            'holiday_comment': 'Comment'
        }

        widgets = {
            'holiday_number': forms.NumberInput(attrs={'class': 'form-control'}), 
            'holiday_type': forms.TextInput(attrs={'class': 'form-control'}), 
            'holiday_description': forms.TextInput(attrs={'class': 'form-control'}), 
            'holiday_from': forms.TextInput(attrs={'class': 'form-control'}),
            'holiday_to': forms.TextInput(attrs={'class': 'form-control'}), 
            'holiday_status': forms.TextInput(attrs={'class': 'form-control'}), 
            'holiday_start_date': DatePickerInput(attrs={'class': 'form-control'}),
            'holiday_end_date': DatePickerInput(attrs={'class': 'form-control'}), 
            'holiday_budget': forms.NumberInput(attrs={'class': 'form-control'}), 
            'holiday_comment': forms.TextInput(attrs={'class': 'form-control'})
        }

class ShoppingForm(forms.ModelForm):
    class Meta:
        model = Shopping
        fields = ['shopping_list_number', 'shopping_description', 'shopping_market', 'shopping_quantity', 'shopping_status', 'shopping_budget','shopping_deadline', 'shopping_comment']
        labels ={
            'shopping_list_number': 'List number', 
            'shopping_description': 'Description', 
            'shopping_market': 'Market', 
            'shopping_quantity': 'Quantity', 
            'shopping_status': 'Status', 
            'shopping_budget': 'Budget', 
            'shopping_deadline': 'Deadline',
            'shopping_comment': 'Comment'
        }

        widgets = {
            'shopping_list_number': forms.NumberInput(attrs={'class': 'form-control'}), 
            'shopping_description': forms.TextInput(attrs={'class': 'form-control'}), 
            'shopping_market': forms.TextInput(attrs={'class': 'form-control'}),
            'shopping_quantity': forms.NumberInput(attrs={'class': 'form-control'}), 
            'shopping_status': forms.TextInput(attrs={'class': 'form-control'}), 
            'shopping_budget': forms.NumberInput(attrs={'class': 'form-control'}), 
            'shopping_deadline': DatePickerInput(attrs={'class': 'form-control'}), 
            'shopping_comment': forms.TextInput(attrs={'class': 'form-control'})
        }

