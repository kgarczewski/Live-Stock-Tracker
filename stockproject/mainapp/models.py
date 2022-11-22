from django.db import models

# Create your models here.
class Stock(models.Model):
    name = models.CharField(max_length=50)
    symbol = models.CharField(max_length=50)
    price = models.FloatField(default=0, blank=0)
    image = models.URLField(blank=True, null=True)

    def __str__(self):
        return str(self.name)
