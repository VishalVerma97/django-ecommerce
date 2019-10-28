from django.urls import path
from .views import HomeView, ItemDetailView

urlpatterns = [
    path('', HomeView.as_view(), name='item-list'),
    # path('checkout/', check_out, name='check-out'),
    path('product/<slug>/', ItemDetailView.as_view(), name="product")
]
