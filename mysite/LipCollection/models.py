from django.db import models


class LipItem(models.Model):
    def __str__(self):
        return self.Name

    Name = models.CharField(max_length=200)
    Brand = models.CharField(max_length=200)
    Flavor = models.CharField(max_length=200)
    Category = models.CharField(max_length=200)
    Picture = models.ImageField(default='lipItem.PNG', upload_to='pictures')
    Price = models.IntegerField()
    Rarity = models.CharField(max_length=200)
