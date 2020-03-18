from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=30, verbose_name='Área')

    def __str__(self):
        return self.name