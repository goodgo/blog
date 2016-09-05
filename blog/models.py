# coding:utf-8

from django.db import models

class Publisher(models.Model):
    name = models.CharField(max_length=30)
    addr = models.CharField(max_length=60)
    city = models.CharField(max_length=20)
    state_province = models.CharField(max_length=20)
    contry = models.CharField(max_length=20)
    website = models.CharField(max_length=40)

    def __unicode__(self):
        return u'%s' % self.name

class Auther(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(blank=True)

    def __unicode__(self):
        return u'name : %s.%s' % (self.last_name, self.first_name)

class Book(models.Model):
    title = models.CharField(max_length=30)
    authers = models.ManyToManyField(Auther)
    publisher = models.ForeignKey(Publisher)
    publish_date = models.DateField()

    def __unicode__(self):
        return u'title: %s | authers: %s | publisher: %s | date: %s ' % (self.title, self.authers, self.publisher, self.publish_date)
