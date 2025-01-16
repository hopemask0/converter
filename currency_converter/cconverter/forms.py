from django import forms

class ConversionForm(forms.Form):
    source_currency = forms.CharField(max_length=3, label='Исходная валюта')
    target_currency = forms.CharField(max_length=3, label='Целевая валюта')
    amount = forms.DecimalField(max_digits=10, decimal_places=2, label='Количество')