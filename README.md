# Backend: (Django) - Project for Assesment
# Name : Employee Management

## About this System
```text
This is a simple web app for employee management which is basically built by focusing on backend.
Key Features ot this Web App :
1. Register
2. Login and Logout
3. Create Employee
4. Update Employee Information
5. Delete Employee
```

## Brief Description of the System
```text
1. User Authentication
Login, Register and Logout are implemented to authenticate users. A new user must have to create an account and
then login to access the employee information.

2. Database Migrations  
There were created models for four table and those tables are :
  a. Employees Table : This table contains name, email, phone, address and department id of employee.
  b. Departments Table : This table contains department name and id.
  c. Achievements Table : This table contains id and nae of the achivement(s).
  d. Pivot Table : This table is for associating employees with achievement(s).

3. Model Relationship
There are basically two model relationship were established : 
  a. One to one between Department and Employee
  b. Many to many between Employee and Achievement

4. Views/Controllers
Most focused features of django views are:
  a. Employee List : Retrive the employee name, department and achievements.
  b. Create Employee : Creates new employee with name, department and achievements.
  c. Update Employee : Update the employee's name, department, and associated achievements.
  d. Delete Employee : Delete employee from database.

5. Database
 Database : SQLite relational database
 Operation : Django ORM 
```

## Class Diagram of the System
```plaintext
+-------------------+       +---------------------+
|    Department     |       |      Achievement    |
+-------------------+       +---------------------+
| - id: Integer     |       | - id: Integer       |
| - name: String    |       | - name: String      |
+-------------------+       +---------------------+
         | 1                             | *
         |                               |
         |                               |
         |                               |
         | *                             | *
+-------------------+       +---------------------------+
|     Employee      |       |      AchievementEmployee   |
+-------------------+       +---------------------------+
| - id: Integer     |       | - id: Integer             |
| - name: String    |       | - achievement: ForeignKey |
| - email: String   |       | - employee: ForeignKey    |
| - phone: String   |       | - achievement_date: DateTime |
| - address: String |       +---------------------------+
| - department: ForeignKey |
+-------------------+
```
## Simple State Diagram of the System

![django](django.png)


## Backend Validation : The crucial step
```text

The app's functionalities and inputs were validated from backed.
  - Register and Login are validated from backend .
  - Input types(digits for number, non digit in name, valid email), Required Data(name and department can not be empty)
  are validated.
```

## Additional Features
```text

HTML and CSS based static pages are created for rendering. For rendering raw HTML and CSS is used instead of
frontend frameworks.
Following pages was rendered and design :
- Login
- Register
- Employee List
- Create Employee
- Update Employee
```

## Technology
```text

Backend : Django
Render : HTML
Database : SQLite
Version Control : Git
```

# Run this web app in local Machine

## Requirements
- Python
- Django

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/1707073Jafril/django-employee.git
    cd EmployeeManagement
    ```
    Or simply download the project file, extract it and go to folder `EmployeeManagement` and open terminal.

2. Create a virtual environment:(Optional)
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install dependencies:
    ```bash
    pip install django
    ```
4. Run makemigrations:(Required if you modify the model)
   ```bash
   python manage.py makemigrations
   ```

5. Run migrates:
    ```bash
    python manage.py migrate
    ```

6. Add Departments from the Django Shell. Run commands sequentially:
   I keep this option to add department through terminal so that this system can be used in different companies where differents departments are available.
    ```bash
    python manage.py shell
    ```
    Then run following commands:
   ```python
   from employee.models import Department
   ```
   ```python
     Department.objects.create(name='HR')
   ```
   ```python
    Department.objects.create(name='Engineering')
   ```
   More department can be added via run the command : `Department.objects.create(name='dept_name')`

   ```python
   exit()
   ```

8. Start the development server:
    ```bash
    python manage.py runserver
    ```
