from django.db import models


class Post(models.Model):
    name = models.CharField(max_length=30, verbose_name='Cargo')

    def __str__(self):
        return self.name
