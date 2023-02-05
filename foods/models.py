from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Item(models.Model):
    
    def __str__(self):
        return self.item_name
    
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.DecimalField(max_digits=10, decimal_places=2)
    item_image = models.CharField(max_length=500, default="https://w7.pngwing.com/pngs/200/109/png-transparent-cooking-pizza-pasta-android-delicious-pizza-thumbnail.png")
    
    def get_absolute_url(self):
        return reverse("foods:detail", kwargs={"pk": self.pk})
    
    