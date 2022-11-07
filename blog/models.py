from django.db import models

class Task(models.Model):
    title = models.CharField('Называние', max_length= 100)
    task = models.TextField('Описание')

    def __str__(self):
        return self.title
