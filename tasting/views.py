from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from .models import Wine, Tasting
from .forms import WineForm, TastingForm


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
    form_class = WineForm
    form = form_class(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            name = form.cleaned_data.get("Name")
            vineyard = form.cleaned_data.get("Vineyard")
            vintage = form.cleaned_data.get("Vintage")
            color = form.cleaned_data.get("Color")
            wine = Wine(Name=name, Vineyard=vineyard, Vintage=vintage, Color=color)
            wine.save()
            return HttpResponseRedirect('/')

    return render(request, 'tasting/add_wine.html', {'form': form})


def add_tasting(request, wine_id):
    this_wine = Wine.objects.get(pk=wine_id)
    form_class = TastingForm
    form = form_class(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            date = form.cleaned_data.get("date")
            hue = form.cleaned_data.get("hue")
            clarity = form.cleaned_data.get("clarity")
            nose = form.cleaned_data.get("nose")
            flavor = form.cleaned_data.get("flavor")
            body = form.cleaned_data.get("body")
            acidity = form.cleaned_data.get("acidity")
            tannin = form.cleaned_data.get("tannin")
            sweetness = form.cleaned_data.get("sweetness")
            fruitiness = form.cleaned_data.get("fruitiness")
            finish = form.cleaned_data.get("finish")
            did_like = form.cleaned_data.get("did_like")
            worth_price = form.cleaned_data.get("worth_price")
            would_buy_again = form.cleaned_data.get("would_buy_again")
            tasting = Tasting(wine=this_wine, date=date, hue=hue, clarity=clarity, nose=nose, flavor=flavor,
                              body=body, acidity=acidity, tannin=tannin, sweetness=sweetness, fruitiness=fruitiness,
                              finish=finish, did_like=did_like, worth_price=worth_price,
                              would_buy_again=would_buy_again)
            tasting.save()
            return HttpResponseRedirect('/')

    return render(request, 'tasting/add_tasting.html', {'wine': this_wine, 'form': form})