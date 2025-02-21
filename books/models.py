from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=120)
    status = models.CharField(max_length=20, choices=[("reading","Reading"),("read","Read"),("toread","Will Read")])
