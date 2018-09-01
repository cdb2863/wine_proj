from django.db import models


# Create your models here.
class Wine(models.Model):
    Name = models.CharField(max_length=200)
    Vineyard = models.CharField(max_length=200)
    Vintage = models.CharField(max_length=4)
    Color = models.CharField(max_length=5)

    def __str__(self):
        rtn = "{} - {} ({})".format(self.Vineyard, self.Name, self.Vintage)
        return rtn


class Tasting(models.Model):
    wine = models.ForeignKey(Wine, on_delete=models.CASCADE)
    date = models.DateTimeField()
    color = models.CharField(max_length=200)
    clarity = models.CharField(max_length=200)
    nose = models.CharField(max_length=200)
    body = models.CharField(max_length=200)
    acidity = models.CharField(max_length=200)
    tannin = models.CharField(max_length=200)
    sweetness = models.CharField(max_length=200)
    fruitiness = models.CharField(max_length=200)
    finish = models.CharField(max_length=200)
    did_like = models.BooleanField()
    worth_price = models.BooleanField()
    would_buy_again = models.BooleanField()

    def __str__(self):
        rtn = "{} on {}".format(self.wine.Name, self.date)
        return rtn


'''
The Six S Evaluation of Wine

1. Sight
    Color
    Clarity
2. Smell
    Immediate smell - nose.
3. Swirl, Smell again.
4. Sip/suck.
    Body
    Acidity
    Tannin
    Sweetness
    Fruitiness
5. Swallow.
    Finish
6. Savor
    Did you like the wine
    Was it worth its price
    Would you buy it again
'''