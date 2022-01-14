from pydoc import describe
from pyexpat import model
from tabnanny import verbose
from turtle import title
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Notes(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    description=models.TextField() 

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name="notes"
        verbose_name_plural="notes"



class Homework(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    subject=models.CharField(max_length=50)
    title=models.CharField(max_length=100)
    description=models.TextField()
    due=models.DateTimeField()
    isFinished=models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.subject+"-"+self.title


    