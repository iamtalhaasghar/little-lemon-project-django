from django.db import models
from django.db import models

# Create your models here.

class MenuItem(models.Model):
    
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=512)
    price = models.IntegerField()

    def __str__(self):
        return f'{self.name} ${self.price}'

    def get_absolute_url(self):
        return reverse("menuitem_detail", kwargs={"pk": self.pk})
