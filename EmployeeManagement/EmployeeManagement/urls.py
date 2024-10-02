from django.contrib import admin
from employee import views
from django.shortcuts import redirect
from django.contrib import admin
from django.urls import include, path


# Setting the urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register, name='register'), 
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('employees/', views.list_employees, name='list_employees'),
    path('', lambda request: redirect('login')),
    path('', include('employee.urls')), 
]
