from django.urls import path

from . import views

app_name = "order"

urlpatterns = [
    path("", views.index, name="index"),
    path("menu/<slug:restaurant>/", views.menu, name="menu"),
    path("menu/<slug:restaurant>/<slug:category>/", views.menu, name="category_menu"),
    path("category/<slug:slug>/", views.category, name="category"),
    path("search/", views.search, name="search"),
    path("cart/", views.cart, name="cart"),
    path("order/", views.order, name="order"),
    path("history/", views.history, name="history")
]