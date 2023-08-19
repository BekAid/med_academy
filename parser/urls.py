from django.urls import path
from . import views

urlpatterns = [
    path('parser_item/', views.ParserFormView.as_view(), name='parser_form'),
    path('item_list/', views.NoutListView.as_view(), name='film_list'),
]