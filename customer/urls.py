from django.urls import path
from .import views 
urlpatterns = [
    path('delivery/', views.Delivery.as_view(),name='delivery'),
    path('about/', views.About.as_view(),name='about'),
    path('order/', views.Order.as_view(),name='order'),
    path('menu/', views.Menu.as_view(),name='menu'),
    path('menu/search/', views.MenuSearch.as_view(),name='menu-search'),
   
]