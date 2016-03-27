from __future__ import unicode_literals

from django.db import models

# Create your models here.

class webBoard(models.Model):
    urlCode = models.TextField()
    name = models.TextField()
    def __unicode__(self) :
        return '%s'%(self.name)

class webDoc(models.Model):
    board = models.ForeignKey(webBoard)
    title = models.TextField()
    content = models.TextField(blank = True)
    date = models.DateField(auto_now = True)
    def __unicode__(self) :
        return '%s-%s'%(self.title, self.date)


class webSNS(models.Model):
    password = models.TextField()
    content = models.TextField()
    date = models.DateField(auto_now = True)
    def __unicode__(self) :
        return '%s-%s'%(self.title, self.date)
