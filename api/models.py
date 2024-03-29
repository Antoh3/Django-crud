from django.db import models

class Crud(models.Model):
    first_name =models.CharField(max_length=100)
    last_name =models.CharField(max_length=100)
    age =models.IntegerField()
    gender =models.CharField(max_length=10)
    grade =models.CharField(max_length=6)
    address =models.TextField()
    contact_number= models.CharField(max_length=20)

    

    def __str__(self) -> str:
        return self.first_name
