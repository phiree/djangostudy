from django.utils import timezone
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import  reverse
from django.views import generic
from products.models import Product


class IndexView(generic.ListView):
    template_name='products/index.html'
    context_object_name='side_product_list'
    def get_queryset(self):
        return Product.objects.all()
    
class SideListView(generic.ListView):
    template_name='produts/side.html'
    context_object_name='side_product_list'
    def get_queryset(self):
        return Product.objects.all()
    
