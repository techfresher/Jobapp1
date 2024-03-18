from django.utils.text import slugify
from django.db import models

# Create your models here.
class Skills(models.Model):
    name = models.CharField(max_length = 150)




class Author(models.Model):
    name = models.CharField(max_length=150)
    company = models.CharField(max_length=150)
    designatiom = models.CharField(max_length=150)

class Location(models.Model):
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    zip = models.CharField(max_length=100)

class Jobpost(models.Model):
    JOB_TYPE_CHOICES = {
        ('Full Time', 'Full Time'),
        ('Part Time', 'Part Time'),
    }
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    expire = models.DateField(null = True)
    salary = models.IntegerField()
    slug = models.SlugField(null=True, max_length=30, unique=True)
    location = models.OneToOneField(Location, on_delete=models.CASCADE,null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    skills = models.ManyToManyField(Skills)
    type = models.CharField(max_length = 150, null=False, choices = JOB_TYPE_CHOICES)
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        return super(Jobpost, self).save(*args, **kwargs)
 
    def __str__(self):
        return f"{self.title} with salary {self.salary}"
    

    # title = models.CharField(max_length=100),
    # description = models.CharField(max_length=50),
    # date = models.DateTimeField(auto_now_add=True),
    # salary = models.IntegerField()