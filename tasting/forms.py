from django import forms
from .models import Wine, Tasting


class WineForm(forms.ModelForm):

    class Meta:
        model = Wine
        fields = ('Name', 'Vineyard', 'Vintage', 'Color')


class TastingForm(forms.ModelForm):

    class Meta:
        model = Tasting
        fields = ('date', 'color', 'clarity', 'nose', 'body', 'acidity', 'tannin', 'sweetness', 'fruitiness', 'finish', 'did_like', 'worth_price', 'would_buy_again')
