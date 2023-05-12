from django.db import models

# Create your models here.


class Picture(models.Model):
    title=models.CharField(max_length=200)
    file=models.ImageField(null=True)
    description=models.TextField()

    def __str__(self):
        return self.title

