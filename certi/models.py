from django.db import models

# Create your models here.
class Certi(models.Model):
    title = models.TextField(max_length=50)
    CertiID = models.TextField(max_length=50)
    institute = models.TextField(max_length=100)
    date = models.DateField()

"""steps to create app
1. python3 manage.py startapp appname
2. create model class in models.py
3. add app detils to project settings.py file
4. make migration
5. migration
6. add detils to admin.py of app"""
