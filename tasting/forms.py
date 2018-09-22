from django import forms
from .models import Wine, Tasting


class WineForm(forms.ModelForm):

    class Meta:
        model = Wine
        fields = ('Name', 'Producer', 'Vintage', 'Color')


class TastingForm(forms.ModelForm):

    class Meta:
        model = Tasting
        fields = ('date', 'hue', 'clarity', 'nose', 'flavor', 'body', 'acidity', 'tannin', 'sweetness', 'fruitiness', 'finish', 'did_like', 'worth_price', 'would_buy_again')
        widgets = {
            'date': forms.DateInput(
                attrs={'type': 'date'}
            )
        }
