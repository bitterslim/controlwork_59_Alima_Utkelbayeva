from django.db import models
from django.db.models import TextChoices


class StatusChoice(TextChoices):
    ACTIVE = 'ACTIVE', 'Active'
    NOT_ACTIVE = 'NOT_ACTIVE', 'Not active'


class Guest(models.Model):
    user = models.CharField(max_length=100, null=False, blank=False, verbose_name='User name')
    email = models.EmailField(max_length=150, null=False, blank=False, verbose_name='Email')
    text = models.TextField(max_length=1000, null=False, blank=False, verbose_name='Text')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    update_date = models.DateTimeField(auto_now=True, verbose_name='Updated at')
    status = models.CharField(max_length=100, null=False, blank=False, default=StatusChoice.ACTIVE,
                              verbose_name='Status')

    def __str__(self):
        return f'{self.user} - {self.email}'
