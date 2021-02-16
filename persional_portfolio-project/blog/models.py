from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    shortDescription = models.CharField(max_length=1000)
    mainBody = models.TextField(max_length=20000)
    image1 = models.ImageField(upload_to = "blog/images/")
    image2 = models.ImageField(upload_to = "blog/images/", blank=True)

    def __str__(self):
        return self.title