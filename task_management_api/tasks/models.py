from django.db import models



class Task(models.Model):
    # список кортежей, который определяет возможные статусы задачи
    STATUS_CHOICES = [
        ('TODO', 'To Do'),
        ('IN_PROGRESS', 'In Progress'),
        ('DONE', 'Done'),
    ]

    title = models.CharField(max_length=200) # поле для названия задачи
    description = models.TextField()         # описание
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='TODO') # для хранения статуса задачи
    deadline = models.DateTimeField()               # срок выполнения задачи
    created_at = models.DateTimeField(auto_now=True) # автоматом заполняется текущей датой и временем при создании новой записи
    updated_at = models.DateTimeField(auto_now=True) # автоматически обновляется текущей датой и временем каждый раз, когда объект модели сохраняется

    def __str__(self):
        return self.title

