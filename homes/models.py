from django.db import models

from django.urls import reverse

from managers.models import Manager


class Category(models.Model):
    category = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.pk} - {self.category}'


class Home(models.Model):
    objects = None
    title = models.CharField(max_length=200, blank=True, null=True)
    info = models.TextField()
    s = models.FloatField()
    district = models.CharField(max_length=200)
    cost = models.IntegerField()
    img = models.ImageField(upload_to='img', blank=True, null=True)
    manager = models.ForeignKey(Manager, on_delete=models.PROTECT, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail_page', args=[self.id])
