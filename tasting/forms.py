from django import forms
from .models import Wine


class WineForm(forms.ModelForm):

    class Meta:
        model = Wine
        fields = ('Name', 'Vineyard', 'Vintage', 'Color')
