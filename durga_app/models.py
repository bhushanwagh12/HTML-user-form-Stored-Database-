from django.db import models

class ContactData(models.Model):
    name=models.CharField(max_length=20)
    salary=models.FloatField()
    email=models.EmailField(max_length=20)
    city=models.CharField(max_length=20)

    def __str__(self):
        return self.name