# В вашем файле forms.py
from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    medicine_id = forms.IntegerField(widget=forms.HiddenInput())

    class Meta:
        model = Order
        fields = ['pharmacy', 'delivery_address', 'full_name', 'phone_number']
        widgets = {
            'pharmacy': forms.Select(attrs={'class': 'form-control'}),
            'delivery_address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите Address'}),
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите имя и фамилию'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите номер телефона'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['medicine_id'].widget = forms.HiddenInput()
