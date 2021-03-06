from django.db import models


class Post(models.Model):
    abbreviation = models.CharField(max_length=30, verbose_name='Sigla', default='-')
    full_name = models.CharField(max_length=255, verbose_name='Nome Cargo', blank=True, null=True)

    def __str__(self):
        return self.abbreviation
