from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search_estate_data, name='search_estate_data'),
    path('get_estate_data/', views.get_estate_data, name='get_estate_data'),

]
