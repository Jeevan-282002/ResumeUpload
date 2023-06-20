from django.db import models

# Create your models here.

class ResumeModel(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    dob = models.DateField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    programming_language = models.CharField(max_length=100)
    education = models.CharField(max_length=100)
    prefered_loc = models.CharField(max_length=100)
    prof_image = models.ImageField(upload_to='Profile_Image/',blank=True)
    project = models.TextField()




