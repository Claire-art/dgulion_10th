from asyncore import write
from csv import writer
from django.db import models

# Create your models here.

class Blog(models.Model) :
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=100)
    pub_data = models.DateTimeField()
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:20]
