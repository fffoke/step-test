from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    user_image = models.ImageField(
        blank=True,
        null=True,
        help_text='Фото профеля (400x400)',
        upload_to='user_image/',
    )
    USER_ROLE=(
        ('customer','Покупатель'),
        ('seller','Продовец')
    )
    role=models.CharField(max_length=20, choices=USER_ROLE, default='customer')
    phone_number=models.CharField(max_length=32)
    def is_customer(self):
        return self.role=='customer' or self.groups.filter(name='customer').exists()
    
    def is_seller(self):
        return self.role=='seller' or self.groups.filter(name='seller').exists()
    
    def __str__(self):
        return self.username
    
class Seller(models.Model):
    user=models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    rating=models.DecimalField(max_digits=3, decimal_places=2, default=0.0)
    balance=models.DecimalField(max_digits=12, decimal_places=2, default=0.0)
    payout_details=models.JSONField(default=dict, blank=True)

    def __str__(self):
        return self.user.username
