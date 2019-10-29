from django.shortcuts import render, get_object_or_404
from .models import Item, OrderItem, Order
from django.views.generic import ListView, DetailView


# Create your views here.


# def item_list(request):
#     context = {
#         'items': Item.objects.all()
#     }
#     return render(request, 'home.html', context)
#
#
def check_out(request):
    return render(request, 'checkout-page.html')

#
# def product(request):
#     context = {
#         'items': Item
#     }
#     return render(request, 'product.html', context)

# we can try to use it like view as
# class HomeView(ListView):
#     model = Item
#     template_item = "home.html"
#     with method inside that class
#     then in path use Home.asView(), in html for loop we use object_list


class HomeView(ListView):
    model = Item
    template_name = "home.html"


class ItemDetailView(DetailView):
    model = Item
    template_name = "product.html"


def add_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_item = OrderItem.objects.create(item= item)
