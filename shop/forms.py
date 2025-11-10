from PIL import Image
import string
from django import forms
from .models import *
from django.core.exceptions import ValidationError
import os


class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields=('title','category','description','image','stock_units','price')
        exclude=('seller',)

    def clean_title(self):
        spec = string.punctuation
        title = self.cleaned_data.get('title')
        if spec in title:
            return ValidationError("В названии не должно быть спец символов")
        return title
    
    def clean_image(self):
        # image = Image.open(self.cleaned_data.get('image'))
        # if image.size > 5:
        #     return ValidationError("В названии не должно быть спец символов")
        image = self.cleaned_data.get('image')
        if image.size >= 5 * 1024 * 1024:
            return ValidationError("Файл должен весить менее 5 мб")
        return image
    
    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 100:
            return ValidationError("минимальная цена 100")
        return price
        





