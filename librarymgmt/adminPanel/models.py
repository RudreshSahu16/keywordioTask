from django.db import models
from django.db.models.base import Model
# Create your models here.
class AddBooks(models.Model):
    bookId=models.AutoField(primary_key=True)
    bookName=models.CharField(max_length=100)
    bookAuthor=models.CharField(max_length=100)
    bookZone=models.CharField(max_length=50)
    bookYear=models.IntegerField()

    def __str__(self):
        return (self.bookName)
