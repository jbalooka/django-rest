from django.db import models
import uuid

TICKET_STATUS = ['WAITING', 'RUNNING', 'FINISHED', 'FAILED', 'WAITING']

class Ticket(models.Model):
    created = models.DateTimeField(auto_now_add=True, auto_now=True)
    id = models.UUIDField(unique = True, editable = False, primary_key = True, default = uuid.uuid4)
    status = models.CharField(choices=TICKET_STATUS, default='WAITING', max_length=10)

    class Meta:
        app_label = 'TC DATA Importer'
        db_table = 'tickets'
        managed = True
        verbose_name = 'Ticket'
        verbose_name_plural = 'Tickets'
        ordering = ('created')