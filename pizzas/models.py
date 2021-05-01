from django.db import models

# Create your models here.

class Pizza(models.Model):
    name=models.CharField(max_length=50)
    

    def __str__(self):
        return self.name

class Topping(models.Model):
    pizza=models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Comment(models.Model):
    pizza=models.ForeignKey(Pizza, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

"""
class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title
"""