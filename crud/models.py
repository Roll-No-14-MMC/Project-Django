from django.db import models

# If a new class is added to models we need to first make migrations 
# and then migrate commands to perform them are:
# 1. python manage.py makemigrations
# 2. python manage.py migrate

# Class denotes table name class variables denotes column names
class Student(models.Model):
    name = models.CharField(max_length = 100)
    roll_number = models.CharField(max_length = 100)
    age = models.IntegerField()

    # This function is a constructor that returns name when a class
    # initialized 
    def __str__(self) -> str:
        return f"{self.name}"

class Teacher(models.Model):
    name = models.CharField(max_length = 100)
    subject = models.CharField(max_length = 100)
    phone = models.BigIntegerField()

    # This function is a constructor that returns name when a class
    # initialized 
    def __str__(self) -> str:
        return (f'{self.name}')
