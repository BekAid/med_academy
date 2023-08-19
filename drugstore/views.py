from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . import models, forms
from django.views import generic

#не полная информация

class OrderView(generic.ListView):
    template_name = 'ordershow.html'
    queryset = models.Order.objects.all

    def get_queryset(self):
        return models.Order.objects.all()

class DrugView(generic.ListView):
    template_name = 'drugshow.html'
    queryset = models.ProductForMedicine.objects.all

    def get_queryset(self):
        return models.ProductForMedicine.objects.all()


