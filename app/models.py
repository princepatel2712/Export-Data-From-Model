from django.db import models


class Book(models.Model):
    author = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    publication_date = models.DateField()
    pages = models.IntegerField()


class FileSave(models.Model):
    file = models.FileField()
