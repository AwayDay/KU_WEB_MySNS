from __future__ import unicode_literals

from django.db import models

# Create your models here.

class webSNS(models.Model):
    password = models.TextField()
    content = models.TextField()
    date = models.DateField(auto_now = True)
    def __unicode__(self) :
        return '%s-%s'%(self.content, self.date)
