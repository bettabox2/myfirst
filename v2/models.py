from django.db import models
# Create your models here.

class Profession(models.Model):
  name = models.CharField(max_length=40)
  type = models.CharField(max_length=40)
  icon = models.CharField(max_length=100)
  description = models.TextField(max_length=255)

  def __str__(self):
      return self.name
        
class Raid(models.Model):
  name = models.CharField(max_length=40)
  addon = models.CharField(max_length=40)
  img = models.CharField(max_length=100)

  def __str__(self):
      return self.name

class HeroClass(models.Model):
  name = models.CharField(max_length=40)
  img = models.CharField(max_length=100)

  def __str__(self):
      return self.name

class Race(models.Model):
  name = models.CharField(max_length=40)
  fraction = models.CharField(max_length=40)
  img = models.CharField(max_length=100)

  def __str__(self):
      return self.name