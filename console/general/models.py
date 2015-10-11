from django.db import models
from console.login.models import Variant


class Dimensions(models.Model):
    class Meta:
        db_table = 'dimensions'

    variant = models.ForeignKey(Variant)
    length = models.FloatField()
    width = models.FloatField()
    height = models.FloatField()
    wheelbase = models.FloatField()
    bootspace = models.FloatField()
    kerbweight = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
