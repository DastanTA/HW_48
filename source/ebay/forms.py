from django import forms
from django.forms import widgets


CATEGORY_CHOICES = [('food', 'еда'), ('toys', 'игрушки'), ('stationary', 'канцелярия'),
                    ('books', 'книги'), ('other', 'другое')]


class ProductForm(forms.Form):
    category = forms.CharField(
        max_length=100, required=True,
        label='категория', widget=forms.Select(choices=CATEGORY_CHOICES)
    )
    name = forms.CharField(max_length=100, required=True, label='Наименование')
    price = forms.DecimalField(max_digits=7, decimal_places=2, required=True, label='цена')
    remainder = forms.IntegerField(min_value=0, required=True, label='остаток')
    description = forms.CharField(
        max_length=2000, required=False,
        label='описание', widget=forms.Textarea(attrs={"cols":30, "rows": 3})
    )
