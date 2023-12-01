# В вашем файле forms.py
from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    medicine_id = forms.IntegerField(widget=forms.HiddenInput())
    quantity = forms.IntegerField(min_value=1, initial=1, widget=forms.NumberInput(attrs={'class': 'form-control', 'style': 'width: 50px;'}))

    class Meta:
        model = Order
        fields = ['pharmacy', 'full_name', 'phone_number', 'quantity']
        widgets = {
            'pharmacy': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Выберите аптеку'}),
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите имя и фамилию'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите номер телефона'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['medicine_id'].widget = forms.HiddenInput()
