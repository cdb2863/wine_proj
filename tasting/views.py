from django.shortcuts import render
from django.http import Http404
from .models import Wine, Tasting


# Create your views here.
def index(request):
    wines = Wine.objects.order_by('Name')
    context = {'wines': wines}
    return render(request, 'tasting/index.html', context)


def wine_detail(request, wine_id):
    try:
        this_wine = Wine.objects.get(pk=wine_id)
        tastings = Tasting.objects.filter(wine = this_wine)
    except Wine.DoesNotExist:
        raise Http404("Wine not found!")
    return render(request, 'tasting/detail.html', {'wine': this_wine, 'tastings': tastings})
