from django.db import models


class Person(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Shoe(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    size = models.SmallIntegerField()
    color = models.CharField(max_length=20)
