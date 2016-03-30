from __future__ import unicode_literals

from django.db import models

# Create your models here.

class webSNS(models.Model):
    password = models.CharField(max_length=32)
    content = models.TextField()
    date = models.DateField(auto_now = True)
    #date = models.DateTimeField(auto_now = True)
    def __unicode__(self) :
        return '%s-%s'%(self.content, self.date)
