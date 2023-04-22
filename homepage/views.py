from django.shortcuts import render
from django.http.response import HttpResponse
from django.views.generic import ListView
from django.views.generic import DetailView

from . import models
# Create your views here.

def index(request):
    return render(request, "homepage/index.html")

def menu(request):
    return render(request, "homepage/menu.html")

class MenuItemListView(ListView):
    model = models.MenuItem

class MenuItemDetailView(DetailView):
    model = models.MenuItem
