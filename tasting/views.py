from django.shortcuts import render
from django.http import Http404
from .models import Wine, Tasting
from .forms import WineForm


# Create your views here.
def index(request):
    wines = Wine.objects.order_by('Name')
    context = {'wines': wines}
    return render(request, 'tasting/index.html', context)


def wine_detail(request, wine_id):
    try:
        this_wine = Wine.objects.get(pk=wine_id)
        tastings = Tasting.objects.filter(wine=this_wine)
    except Wine.DoesNotExist:
        raise Http404("Wine not found!")
    return render(request, 'tasting/detail.html', {'wine': this_wine, 'tastings': tastings})


def tasting_detail(request, tasting_id):
    try:
        this_tasting = Tasting.objects.get(pk=tasting_id)
    except Tasting.DoesNotExist:
        raise Http404("Tasting not found!")
    return render(request, 'tasting/tasting_detail.html', {'tasting': this_tasting})


def add_wine(request):
    form = WineForm()
    return render(request, 'tasting/add_wine.html', {'form': form})
