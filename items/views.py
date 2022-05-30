from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView, FormView, View, RedirectView
import datetime

def home(request):
    dt = datetime.datetime.now()
    context = {
        'title': 'Home',
        'body': 'This is the home page'
    }
    return HttpResponse(request,f"Items page, {dt}")
def display_category(request):
    dt = datetime.datetime.now()
    context = {
        'title': 'Category',
        'body': 'This is the category page'
    }
    return HttpResponse(request,f"display_category page, {dt}")
def display_items(request):
    dt = datetime.datetime.now()
    context = {
        'title': 'Item',
        'body': 'This is the item page'
    }
    return render(request, 'base.html', context)