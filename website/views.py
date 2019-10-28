from django.shortcuts import render
from .models import Item
from django.views.generic import ListView, DetailView


# Create your views here.


# def item_list(request):
#     context = {
#         'items': Item.objects.all()
#     }
#     return render(request, 'home-page.html', context)
#
#
# def check_out(request):
#     return render(request, 'checkout-page.html')
#
#
# def product(request):
#     context = {
#         'items': Item
#     }
#     return render(request, 'product-page.html', context)

# we can try to use it like view as
# class HomeView(ListView):
#     model = Item
#     template_item = "home.html"
#     with method inside that class
#     then in path use Home.asView(), in html for loop we use object_list

class HomeView(ListView):
    model = Item
    template_name = 'home-page.html'


class ItemDetailView(DetailView):
    model = Item
    template_name = 'product-page.html'
