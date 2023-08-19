from django import forms
from . import models

class OrderForm(forms.ModelForm):
    class Meta:
        model = models.Order
        fields = '__all__'

class DrugForm(forms.ModelForm):
    class Meta:
        model = models.ProductForMedicine
        fields = '__all__'