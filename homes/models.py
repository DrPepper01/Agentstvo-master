from django.db import models


class Category(models.Model):
    category = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.pk} - {self.category}'


class Home(models.Model):
    title = models.CharField(max_length=200, blank=True,null=True)
    info = models.TextField()
    s = models.FloatField()
    district = models.CharField(max_length=200)
    cost = models.IntegerField()
    img = models.ImageField(upload_to='img', blank=True, null=True)

    def __str__(self):
        return self.title