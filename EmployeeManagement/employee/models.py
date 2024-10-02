from django.db import models

# Department
class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Achievement
class Achievement(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Employee with the required fields
class Employee(models.Model):
    name = models.CharField(max_length=100)     # Employee Name
    email = models.EmailField(unique=True, blank=True, null= True)   # Employee Email
    phone = models.CharField(max_length=15, blank=True, null= True)  # Employee Phone
    address = models.TextField()                                     # Employee Address
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='employees')  # Relationship with department

    def __str__(self):
        return self.name


# Define a pivot table for associating employees with achievements
class AchievementEmployee(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE)
    achievement_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f'{self.employee.name} - {self.achievement.name}'
