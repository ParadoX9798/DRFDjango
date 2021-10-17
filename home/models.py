from django.db import models


class Car(models.Model):
    model = models.CharField(max_length=50)
    year = models.DateField()

    def __str__(self):
        return f'{self.model} {self.year}'


class Person(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="pcar")
    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    email = models.IntegerField()

    def __str__(self):
        return self.name
