from django.db import models


class Manager(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    img = models.ImageField(upload_to='manager_img')

    def __str__(self):
        return f'{self.id} - {self.first_name}'
