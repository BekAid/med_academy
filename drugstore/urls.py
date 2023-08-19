from django.urls import path
from . import views

urlpatterns = [
    path('ordershow/', views.OrderView.as_view(), name='orders'),
    path('drugshow/', views.DrugView.as_view(), name='drugs'),

    ]