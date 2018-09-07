from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:wine_id>/', views.wine_detail, name='wine_detail'),
    path('tasting_detail/<int:tasting_id>/', views.tasting_detail, name='tasting_detail'),
    path('add_wine/', views.add_wine, name='add_wine'),
    path('<int:wine_id>/add_tasting/', views.add_tasting, name='add_tasting')
]
