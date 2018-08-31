from django.shortcuts import render
from django.http import HttpResponse
from .models import Wine


# Create your views here.
def index(request):
    wines = Wine.objects.order_by('Name')
    context = {'wines': wines}
    return render(request, 'tasting/index.html', context)
