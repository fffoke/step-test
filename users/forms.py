from django import forms
from .models import *
from django.core.exceptions import ValidationError

class SignUpForm(forms.ModelForm):
    password1=forms.CharField(required=True, label='Password', widget=forms.PasswordInput())
    password2=forms.CharField(required=True, label='Confirm Password', widget=forms.PasswordInput())
    class Meta:
        model=CustomUser
        fields=('username','first_name','last_name','email', 'phone_number','user_image','password1','password2', 'role')

    def clean(self):
        cleaned = super().clean()
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password1')
        if password1 != password2:
            return ValidationError("Пароли не совпадают")
        return cleaned
    
    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.get('password1')
        if password:
            user.set_password(password)
        if commit:
            user.save()
            if user.role == 'seller':
                Seller.objects.create(user=user)
        return user

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs['class'] = 'field'

class SignInForm(forms.ModelForm):
    class Meta:
        model=CustomUser
        fields=('username', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs['class'] = 'field'