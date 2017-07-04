from django.db import models

# Create your models here.


class superProfile(models.Model):
    title=models.CharField(max_length=50,blank=True)
    aboutBlog=models.TextField(blank=True)
    aboutAuthor=models.TextField(blank=True)
    phone=models.CharField(max_length=11,blank=True)
    mail=models.CharField(max_length=20,blank=True)
    firstname=models.CharField(max_length=20,blank=True)

    def __str__(self):
        return self.title
