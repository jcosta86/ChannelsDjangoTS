from django.db import models


class Channel(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=255, null=True, blank=True)
    contact = models.CharField(max_length=100, null=False, blank=False)
    url = models.CharField(max_length=100, null=False, blank=False)
    rate = models.FloatField(null=False, blank=False)
    
    def __str__(self):
        return f'{self.name}'



    