from django.db import models

# Create your models here.
class Blogging(models.Model):
  title = models.CharField(max_length=250)
  date = models.DateField()
  description = models.TextField()
  
  def __str__(self):
    return self.title

  # date = models.DateField(auto_now=True)
  # description = models.CharField(max_length=250)