from django.db import models
from django.conf import settings

# 'AutoField' is a class that represents an automatically incrementing integer field in a database table. It is typically used as the primary key field for a model.

class link(models.Model):
    id=models.AutoField(primary_key=True)
    actual_url=models.TextField(default="")
    short_url=models.URLField(blank=True,default=True)
    hit_count=models.IntegerField(default=0)
    expired=models.BooleanField(default=False)