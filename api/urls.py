from django.urls import path

from . import views

urlpatterns = [

    path('orders/', views.Orders.as_view()),
    path('orders/<int:pk>/', views.OrdersDetail.as_view()),
    path('locations/',views.Locations.as_view()),
    path('restaurant/',views.Restaurant.as_view()),
    path('foodlist/',views.FoodList.as_view()),

]