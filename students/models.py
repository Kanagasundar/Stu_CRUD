from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=20,unique=True)
    dob = models.DateField('Date of Birth')
    department = models.CharField(max_length=100)
    year_of_studying = models.IntegerField()

    def __str__(self):
        return self.name