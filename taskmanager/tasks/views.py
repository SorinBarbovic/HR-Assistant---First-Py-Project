from xmlrpc.client import boolean
from django.shortcuts import redirect, render
from .models import Task, Holiday, Shopping #complete
from .forms import TaskForm, HolidayForm, ShoppingForm

from django.views.generic.edit import FormView
# from .filters import TaskFilter

from django.http import HttpResponseRedirect, HttpResponse, HttpRequest
from django.urls import reverse, reverse_lazy


from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
 

class CustomLoginView(LoginView):
    template_name = 'tasks/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self) -> str:
        return reverse_lazy('index')

class RegisterPage(FormView):
    template_name = 'tasks/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('index')

    def form_valid(self, form) -> HttpResponse:
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    #if redirect_auth_user does not work, use below
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse('index')) #or redirect ('index')
        return super(RegisterPage, self).get(*args, **kwargs)

# def get_context_data(self, **kwargs):
#     data = Task.objects.all()
#     data2 = Holiday.objects.all()
#     data3 = Shopping.objects.all()
#     context = {
#         'data' : data,
#         'data2' : data2,
#         'data3' : data3
#     }
#     search_input = self.request.GET.get('search-area') or ''
#     if search_input:
#         context['data'] = context['data'].filter(task_description__startswith=search_input)

@login_required
def index (request):
    # tFilter = TaskFilter()
    return render(request, 'tasks/index.html', {'Task': Task.objects.all()} 
    
    )

def view_task(request, id):
    task = Task.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))

def add_task(request):
    if request.method == 'Post': 
        task_form = TaskForm(request.POST)
        if task_form.is_valid():
            new_task_number = task_form.cleaned_data['task_number'] 
            new_task_name =  task_form.cleaned_data['task_name'] 
            new_task_description =  task_form.cleaned_data['task_description'] 
            new_task_category =  task_form.cleaned_data['task_category'] 
            new_task_status =  task_form.cleaned_data['task_status']
            new_task_created_date =  task_form.cleaned_data['task_created_date']
            new_task_due_date =  task_form.cleaned_data['task_due_date']
            new_task_completed_date =  task_form.cleaned_data['task_completed_date'] 
            new_task_comment =  task_form.cleaned_data['comment']

            new_task = Task (
                task_number = new_task_number,
                task_name = new_task_name,
                task_description = new_task_description,
                task_category = new_task_category,
                task_status = new_task_status,
                task_created_date = new_task_created_date,
                task_due_date = new_task_due_date,
                task_completed_date = new_task_completed_date,
                task_comment = new_task_comment
                )

            new_task.save()
            return render(request, 'tasks/add_task.html',
            {'form': TaskForm(),
            'success': True
            })
    else:
        task_form = TaskForm()
    return render(request, 'tasks/add_task.html', {'form': TaskForm()})

def edit(request, id):
    if request.method == "POST":
        task = Task.objects.get(pk=id)
        task_form = TaskForm(request.POST, instance=task)
        if task_form.is_valid():
            task_form.save()
            return render(request, 'tasks/edit.html',
            {'form': task_form,
            'success': True
            })
    else:
        task = Task.objects.get(pk=id)
        task_form = TaskForm(instance=task)
    return render(request, 'tasks/edit.html', {'form': task_form})

def delete_task(request, id):
    if request.method == "POST":
        task = Task.objects.get(pk=id)
        task.delete()
        return HttpResponseRedirect(reverse('index'))

def complete_task (request, id):
    if request.method == "POST":
        task = Task.objects.get(pk=id)
        task.complete = True
        task.save()
        return HttpResponseRedirect(reverse('index'))

####################### HOLIDAY
@login_required
def holiday (request):
    return render(request, 'tasks/holiday.html', {'holiday': Holiday.objects.all()} 
    
    )

def view_holiday(request, id):
    holiday = Holiday.objects.get(pk=id)
    return HttpResponseRedirect(reverse('holiday'))

def add_holiday(request):
    if request.method == 'Post': 
        holiday_form = HolidayForm(request.POST)
        if holiday_form.is_valid():
            new_holiday_number = holiday_form.cleaned_data['holiday_number'] 
            new_holiday_type =  holiday_form.cleaned_data['holiday_type'] 
            new_holiday_description =  holiday_form.cleaned_data['holiday_description'] 
            new_holiday_from =  holiday_form.cleaned_data['holiday_from'] 
            new_holiday_to =  holiday_form.cleaned_data['holiday_to']
            new_holiday_status =  holiday_form.cleaned_data['holiday_status']
            new_holiday_start_date =  holiday_form.cleaned_data['holiday_start_date']
            new_holiday_end_date =  holiday_form.cleaned_data['holiday_end_date']
            new_holiday_budget =  holiday_form.cleaned_data['holiday_budget'] 
            new_holiday_comment =  holiday_form.cleaned_data['comment']

            new_holiday = Holiday (
                holiday_number = new_holiday_number,
                holiday_type = new_holiday_type,
                holiday_description = new_holiday_description,
                holiday_from = new_holiday_from,
                holiday_to = new_holiday_to,
                holiday_status = new_holiday_status,
                holiday_start_date = new_holiday_start_date,
                holiday_end_date = new_holiday_end_date,
                holiday_budget = new_holiday_budget,
                holiday_comment = new_holiday_comment
                )

            new_holiday.save()
            return render(request, 'tasks/add_holiday.html',
            {'form': HolidayForm(),
            'success': True
            })
    else:
        holiday_form = HolidayForm()
    return render(request, 'tasks/add_holiday.html', {'form': HolidayForm()})

def edit_holiday(request, id):
    if request.method == "POST":
        holiday = Holiday.objects.get(pk=id)
        holiday_form = HolidayForm(request.POST, instance=holiday)
        if holiday_form.is_valid():
            holiday_form.save()
            return render(request, 'tasks/edit_holiday.html',
            {'form': holiday_form,
            'success': True
            })
    else:
        holiday = Holiday.objects.get(pk=id)
        holiday_form = HolidayForm(instance=holiday)
    return render(request, 'tasks/edit_holiday.html', {'form': holiday_form})

def delete_holiday(request, id):
    if request.method == "POST":
        holiday = Holiday.objects.get(pk=id)
        holiday.delete()
        return HttpResponseRedirect(reverse('holiday'))

def complete_holiday (request, id):
    if request.method == "POST":
        holiday = Holiday.objects.get(pk=id)
        complete = True
        holiday.save()
        return HttpResponseRedirect(reverse('holiday'))

####################### SHOPPING
@login_required
def shopping (request):
    return render(request, 'tasks/shopping.html', {'shopping': Shopping.objects.all()} 
    
    )

def view_shopping(request, id):
    shopping = Shopping.objects.get(pk=id)
    return HttpResponseRedirect(reverse('shopping'))

def add_shopping(request):
    if request.method == 'Post': 
        shopping_form = ShoppingForm(request.POST)
        if shopping_form.is_valid():
            new_shopping_list_number = shopping_form.cleaned_data['shopping_list_number'] 
            new_shopping_description =  shopping_form.cleaned_data['shopping_description'] 
            new_shopping_market =  shopping_form.cleaned_data['shopping_market'] 
            new_shopping_quantity =  shopping_form.cleaned_data['shopping_quantity']
            new_shopping_status =  shopping_form.cleaned_data['shopping_status']
            new_shopping_budget =  shopping_form.cleaned_data['shopping_budget']
            new_shopping_deadline =  shopping_form.cleaned_data['shopping_deadline'] 
            new_shopping_comment =  shopping_form.cleaned_data['comment']

            new_shopping = Shopping (
                shopping_list_number = new_shopping_list_number,
                shopping_description = new_shopping_description,
                shopping_market = new_shopping_market,
                shopping_quantity = new_shopping_quantity,
                shopping_status = new_shopping_status,
                shopping_budget = new_shopping_budget,
                shopping_deadline = new_shopping_deadline,
                shopping_comment = new_shopping_comment
                )

            new_shopping.save()
            return render(request, 'tasks/add_shopping.html',
            {'form': ShoppingForm(),
            'success': True
            })
    else:
        shopping_form = ShoppingForm()
    return render(request, 'tasks/add_shopping.html', {'form': ShoppingForm()})

def edit_shopping(request, id):
    if request.method == "POST":
        shopping = Shopping.objects.get(pk=id)
        shopping_form = ShoppingForm(request.POST, instance=shopping)
        if shopping_form.is_valid():
            shopping_form.save()
            return render(request, 'tasks/edit_shopping.html',
            {'form': shopping_form,
            'success': True
            })
    else:
        shopping = Shopping.objects.get(pk=id)
        shopping_form = ShoppingForm(instance=shopping)
    return render(request, 'tasks/edit_shopping.html', {'form': shopping_form})

def delete_shopping(request, id):
    if request.method == "POST":
        shopping = Shopping.objects.get(pk=id)
        shopping.delete()
        return HttpResponseRedirect(reverse('shopping'))

def complete_shopping (request, id):
    if request.method == "POST":
        shopping = Shopping.objects.get(pk=id)
        complete = True
        shopping.save()
        return HttpResponseRedirect(reverse('shopping'))

####################### REPORTS

def reports (request):
    return render(request, 'tasks/report.html', {'reports': Shopping.objects.all()} 
    
    )

def view_report(request, id):
    reports = Shopping.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))


