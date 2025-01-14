from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)
    priority = models.IntegerField(default=1)
    description = models.TextField(default='')
    location = models.CharField(max_length=255, default='')
    organizer = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.name


class Guest(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    mobile = models.BigIntegerField()

    def __str__(self):
        return self.name
