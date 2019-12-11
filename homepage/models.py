from django.db import models

# Create your models here.

class Section(models.Model):
    slug=models.SlugField()
    sectionTitle=models.TextField()
    sectionContent=models.TextField()

class testimonalCard(models.Model):
    slug=models.SlugField()
    imageUrl=models.ImageField(default='xyz')
    cardTitle=models.TextField()
    testimonalContent=models.TextField()

class images(models.Model):
    slug=models.SlugField()
    image=models.ImageField(default='xyz')


#Product Categories

class Arthroscopy(models.Model):
    slug=models.SlugField()
    product=models.TextField()

class Hysteroscopy(models.Model):
    slug=models.SlugField()
    product=models.TextField()

class ContactUs(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    subject=models.CharField(max_length=100)
    message=models.TextField()