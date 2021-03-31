from django.db import models

class Project(models.Model):
  title = models.CharField(max_length=100)
  description = models.CharField(max_length=250)
  image = models.ImageField(upload_to='portfolio/images')
  url = models.URLField(blank=True)    
  #blank is used for url clickable,m will allow entry of an empty value. If a field has blank=False, the field will be required.
  
  def __str__(self):
    return self.title