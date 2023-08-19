from django.urls import path
from . import views

urlpatterns = [

    path('kgmawork/', views.KgmaWorkView.as_view(), name='show'),


    path('kgmawork/<int:id>/', views.KgmaWorkDetailView.as_view(), name='show_detail'),

    path('kgmawork/<int:id>/update/', views.KgmaWorkUpdateView.as_view(), name='update'),


    path('kgmawork/<int:id>/delete/', views.KgmaWorkDeleteView.as_view(), name='delete'),

    path('add-work/', views.KgmaWorkCreateView.as_view(), name='add'),

    path('kgmawork/<int:id>/commentadd/', views.CommentCreateView.as_view(), name='add-comm'),

    path('add-comm/', views.CommentCreateView.as_view(), name='add-comm'),

]