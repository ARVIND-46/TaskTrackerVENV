from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
   # user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    due_date =models.DateField(null=True,blank=True)
    priority =models.CharField(max_length=20 ,choices=[('High','High'),('Medium','Medium'),('Low','Low')])
    status = models.CharField(max_length=20 ,choices=[('Pending','Pending'),('Completed','completed')])
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.tittle

