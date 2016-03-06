from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Write(models.Model):
    name = models.CharField(max_length=20)
    pub_date = models.DateTimeField('date published')
    
    def __unicode__(self):
        return self.name    