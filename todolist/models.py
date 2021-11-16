from django.db import models
from django.urls import reverse

class TaskList(models.Model):
    task = models.CharField(max_length=300)
    done = models.BooleanField(default=False)
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.task + ' - ' + str(self.done) + ' : ' + str(self.time)[:16]
    
    class Meta:
        ordering = ['-time']
    
