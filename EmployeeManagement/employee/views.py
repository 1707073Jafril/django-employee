from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Employee, Department, Achievement, AchievementEmployee
from django.core.exceptions import ValidationError
from django.core.validators import validate_email


# Register for new user
def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        username = email  # Use email as username

        # Validate that email and password are provided
        if not email or not password:
            messages.error(request, 'Both email and password are required.')
        else:
            # Check if the email is already registered
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Email already registered.')
            else:
                # Create the user
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                messages.success(request, 'Registration successful! You can now log in.')
                return redirect('login')  # Redirect to login page after successful registration

    return render(request, 'registration/register.html')

# User login view
def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('list_employees')
        else:
            messages.error(request, 'Invalid email or password.')
            return render(request, 'employee/login.html')

    # Redirect logged in users to the employee list
    if request.user.is_authenticated:
        return redirect('list_employees')

    return render(request, 'employee/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')  # Redirect to login after logout

# List of the employees with department and achievements
@login_required
def list_employees(request):
    # Fetch employees with related department and achievements
    employees = Employee.objects.prefetch_related('department', 'achievementemployee_set__achievement').all()

    employee_data = []
    
    for employee in employees:
        achievements = [achievement.achievement.name for achievement in employee.achievementemployee_set.all()]
        employee_data.append({
            'id': employee.id,
            'name': employee.name,
            'department': employee.department.name if employee.department else 'No Department',
            'achievements': achievements if achievements else ['No Achievements'],
        })

    return render(request, 'employee/list.html', {'employee_data': employee_data})

# Create new user with data

@login_required  
def create_employee(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        department_id = request.POST.get('department')

        # Validate name (must not be numeric and must not be empty)
        if not name or name.isnumeric():
            messages.error(request, 'Name is required and must not be a number.')
            return redirect('create_employee')  # Redirect back to the create page

        department = get_object_or_404(Department, id=department_id)

        # Create the employee
        employee = Employee.objects.create(
            name=name,
            department=department
        )

        # Add achievements
        achievement_names = request.POST.get('achievements').split(',')  

        for achievement_name in achievement_names:
            achievement_name = achievement_name.strip()
            if achievement_name:
                achievement, created = Achievement.objects.get_or_create(name=achievement_name)
                AchievementEmployee.objects.create(
                    employee=employee,
                    achievement=achievement,
                
                )

        messages.success(request, 'Employee created successfully!')
        return redirect('list_employees')

    departments = Department.objects.all()
    return render(request, 'employee/create.html', {'departments': departments})


# Update informations of existing employess

@login_required 
def update_employee(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)

    if request.method == 'POST':
        name = request.POST.get('name')
        department_id = request.POST.get('department')
        achievement_names = request.POST.get('achievements').split(',')

        # Validate required fields
        if not name:
            messages.error(request, 'Name is required.')
            return redirect('update_employee', employee_id=employee.id)  # Redirect back to the update page
        if name.isnumeric():
            messages.error(request, 'Name must not be a number.')
            return redirect('update_employee', employee_id=employee.id)
        
        # Update employee details
        employee.name = name
        employee.department = get_object_or_404(Department, id=department_id)
        employee.save()

        # Get existing achievements for the employee
        existing_achievements = set(ach.achievement.name for ach in employee.achievementemployee_set.all())
        new_achievements = set(achievement_name.strip() for achievement_name in achievement_names if achievement_name.strip())

        # Update or create achievements
        for achievement_name in new_achievements:
            achievement, created = Achievement.objects.get_or_create(name=achievement_name)
            AchievementEmployee.objects.update_or_create(
                employee=employee,
                achievement=achievement
            )

        # Remove achievements that are no longer present
        for achievement in existing_achievements:
            if achievement not in new_achievements:
                AchievementEmployee.objects.filter(employee=employee, achievement__name=achievement).delete()

        messages.success(request, 'Employee updated successfully!')
        return redirect('list_employees')

    departments = Department.objects.all()
    current_achievements = ', '.join([ach.achievement.name for ach in employee.achievementemployee_set.all()])

    return render(request, 'employee/update.html', {
        'employee': employee,
        'departments': departments,
        'current_achievements': current_achievements,
    })



# Delete Employee information
@login_required 
def delete_employee(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    if request.method == 'POST':
        employee.delete()
        return redirect('list_employees')
    return render(request, 'employee/confirm_delete.html', {'employee': employee})
