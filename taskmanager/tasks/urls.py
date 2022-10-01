from django.urls import path
from . import views
from .views import CustomLoginView, RegisterPage

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name = 'login'),
    path('logout/', LogoutView.as_view(next_page='login'), name = 'logout'),
    path('register/', RegisterPage.as_view(), name = 'register'),
    path('', views.index, name = 'index'),
    path('<int:id>', views.view_task, name = 'view_task'),
    path('<int:id>', views.view_holiday, name = 'view_holiday'),
    path('<int:id>', views.view_shopping, name = 'view_shopping'),
    path('add_task/',views.add_task, name='add_task'),
    path('add_holiday/',views.add_holiday, name='add_holiday'),
    path('add_shopping/',views.add_shopping, name='add_shopping'),
    path('edit/<int:id>/',views.edit, name='edit'),
    path('edit_shopping/<int:id>/',views.edit_shopping, name='edit_shopping'),
    path('edit_holiday/<int:id>/',views.edit_holiday, name='edit_holiday'),
    path('delete_task/<int:id>/',views.delete_task, name='delete_task'),
    path('delete_holiday/<int:id>/',views.delete_holiday, name='delete_holiday'),
    path('delete_shopping/<int:id>/',views.delete_shopping, name='delete_shopping'),
    path('holiday', views.holiday, name = 'holiday'),
    path('shopping', views.shopping, name = 'shopping'),
    path('report', views.reports, name = 'report'),
    path('complete_task/<int:id>/',views.complete_task, name='index'),
    path('complete_holiday/<int:id>/',views.complete_holiday, name='holiday'),
    path('complete_shopping/<int:id>/',views.complete_shopping, name='shopping'),

]