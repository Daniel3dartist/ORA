from django.db import models


class MyUser(models.Model):
    username = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    end_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=30)
    ip = models.JSONField(default=None)


class Item(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField()

    def __str__(self):
        return self.name
