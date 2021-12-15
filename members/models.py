from django.db import models

# Create your models here.
class members(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField(max_length=5)
    birth = models.DateTimeField()
    email = models.CharField(max_length=50)

    def __str__(self):
        return f'[{self.pk}] {self.name}'

    def get_absolute_url(self):
        return f'/members/{self.pk}/'