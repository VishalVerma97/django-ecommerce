from django.urls import path
from .views import HomeView, ItemDetailView, check_out


app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('checkout/', check_out, name='check-out'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product')
]
