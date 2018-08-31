from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Wine


# Create your views here.
def index(request):
    wines = Wine.objects.order_by('Name')
    context = {'wines': wines}
    return render(request, 'tasting/index.html', context)

def wine_detail(request, wine_id):
    try:
        wine = Wine.objects.get(pk=wine_id)
    except Wine.DoesNotExist:
        raise Http404("Wine not found!")
    return render(request, 'tasting/detail.html', {'wine': wine})
