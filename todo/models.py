from django.db import models
from django.utils import timezone
 
TASK_STATUS = (
	("OPEN","OPEN"),
	("WORKING","WORKING"),
	("DONE","DONE"),
	("OVERDUE","OVERDUE"),
)

class Todo(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField(max_length=1000)
    date = models.DateTimeField(default=timezone.now)
    taskstatus = models.CharField(
        max_length=20,
	    choices = TASK_STATUS,
	    default = 'OPEN'
    )
    duedate = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title	
