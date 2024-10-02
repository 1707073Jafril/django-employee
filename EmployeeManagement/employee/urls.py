from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('employees/', views.list_employees, name='list_employees'),   # Employee list
    path('employees/create/', views.create_employee, name='create_employee'),   # Add new employee
    path('employees/<int:employee_id>/update/', views.update_employee, name='update_employee'),  # Update employee info
    path('employees/<int:employee_id>/delete/', views.delete_employee, name='delete_employee'),  # DElete employee
]

