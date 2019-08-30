from core.models import UUIDModel
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class List(UUIDModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="user", help_text="User")
    name = models.CharField(max_length=64, verbose_name="name", help_text="Name of the list")

    class Meta:
        ordering = ['name']
        verbose_name = "list"
        verbose_name_plural = "lists"

    def __str__(self):
        return self.name


class Task(UUIDModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="user", help_text="User")
    list = models.ForeignKey(List, on_delete=models.CASCADE, blank=True, null=True,
                             verbose_name="list", help_text="List")
    name = models.CharField(max_length=256, verbose_name="name", help_text="Name of the task")
    notes = models.TextField(blank=True, verbose_name="notes", help_text="Notes for the task")
    due_date = models.DateField(blank=True, null=True, verbose_name="due date", help_text="Due date")
    due_time = models.TimeField(blank=True, null=True, verbose_name="due time", help_text="Due time")
    done = models.BooleanField(default=False, verbose_name="done", help_text="Is done?")

    class Meta:
        ordering = ['list', 'done', 'due_date', 'due_time', 'name']
        verbose_name = "task"
        verbose_name_plural = "tasks"

    def __str__(self):
        return self.name
