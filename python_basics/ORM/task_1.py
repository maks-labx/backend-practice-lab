from django.db import models

class Store(models.Model):
    name = models.CharField(max_length=100)


class Ticket(models.Model):
    store = models.ForeignKey(
        Store,
        on_delete=models.CASCADE,
        related_name="tickets"
    )
    description = models.TextField()
    status = models.CharField(max_length=20)