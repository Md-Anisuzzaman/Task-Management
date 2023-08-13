from django.db import models


class TaskModel(models.Model):
    id = models.AutoField(
        primary_key=True, null=False, blank=False, unique=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
