# В вашем файле forms.py
from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    medicine_id = forms.IntegerField(widget=forms.HiddenInput())
    quantity = forms.IntegerField(min_value=1, max_value=10, initial=1, label='Кількість', widget=forms.NumberInput(attrs={'class': 'form-control', 'style': 'width: 55px;'}))
    price = forms.DecimalField(label='Ціна', widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly', 'style': 'width: 100px;'}))

    class Meta:
        model = Order
        fields = ['pharmacy', 'full_name', 'phone_number', 'quantity', 'price']
        labels = {
            'pharmacy': 'Замовити в аптеку на вулиці:',
            'full_name': 'Повне ім`я:',
            'phone_number': 'Номер телефону:',
        }
        widgets = {
            'pharmacy': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Виберіть аптеку'}),
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введіть ім`я та прізвище'}),
            'phone_number': forms.TextInput(attrs={'type': 'tel', 'class': 'form-control', 'placeholder': 'Введіть номер телефону'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['medicine_id'].widget = forms.HiddenInput()

# 'pattern': "38[0-9]{1}-[0-9]{3}-[0-9]{4}",
