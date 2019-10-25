from django import forms
from .models import (Basket,Item)

class BasketForm(forms.ModelForm):
    class Meta:
        model = Basket
        fields = ('title',)

