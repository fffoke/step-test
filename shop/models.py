from django.db import models
from users.models import Seller

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name

class Product(models.Model):
    title=models.CharField(max_length=150)
    category=models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    description=models.TextField()
    image=models.ImageField(upload_to='Shope/product_imge/')
    stock_units=models.PositiveBigIntegerField(default=0)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    seller=models.ForeignKey(Seller, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
