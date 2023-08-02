from django.db import models

# Create your models here.

class TaskManager(models.Manager):
    def create_task(self,name,priority,progress,dueDate):
        task = self.create(name=name, priority = priority, progress = progress, dueDate = dueDate)
        
        return task

class Task(models.Model):
    name = models.CharField(max_length=50)
    priority = models.CharField( max_length=100)
    dueDate = models.DateField()
    
    objects = TaskManager()
    
    def __str__(self) :
        return (f"task : {self.name}")
    
   

