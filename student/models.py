from django.db import models
class Student(models.Model):
    first_name =models.CharField(max_length=20)
    last_name =models.CharField(max_length=30)
    age=models.IntegerField()

    def  __str__(self) -> str:
        return self.first_name
