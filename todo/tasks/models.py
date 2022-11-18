from django.db import models


class Task(models.Model):

    STATUS = (
        ('1', 'Doing'),
        ('2', 'Done')
    )

    title = models.CharField(max_length=140)
    description = models.TextField(max_length=1000)
    done = models.CharField(max_length=1, choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
