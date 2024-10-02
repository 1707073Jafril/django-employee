# Backend: (Django) - Project for Assesment

```text
This is a simple web app is which is basically built by focusing on backend development.
Key Features ot this Web App :
1. Register
2. Login and Logout
3. Add Employee
4. Edit Employee Information
5. Delete Employee
```

```text
Brief Description of the App

1. User Authentication
Login, Register and Logout are implemented to authenticate users. A new user must have to create an account and then login to access the employee information.

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
