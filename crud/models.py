from django.db import models

# Create your models here.
class GroupType(models.TextChoices):
    PROJEKT = "Projekt"
    LABORATORIUM = "Laboratorium"
    CWICZENIA = "Ćwiczenia"

class Group(models.Model):
    id = models.AutoField(primary_key=True)
    number = models.IntegerField()
    type = models.CharField(max_length=20, choices=GroupType.choices)

    def __str__(self):
        return str(self.type) + ' ' + str(self.number)

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + '' + self.last_name