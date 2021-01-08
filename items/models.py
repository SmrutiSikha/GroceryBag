from django.db import models

# Create your models here.
class Grocery(models.Model):
    ItemName = models.CharField(max_length=100)
    ItemQuantity = models.CharField(max_length=50)
    ItemStatus = models.IntegerField()
    Date = models.DateField()
    UserId = models.IntegerField(default=5)

    def __str__(self):
        return self.ItemName
