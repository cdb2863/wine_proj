from django.urls import  path
from . import  views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:wine_id>/', views.wine_detail, name='wine_detail')
]