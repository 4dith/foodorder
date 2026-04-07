from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from restaurants.models import Restaurant, Category, Item
from order.models import OrderItem, Order

import datetime
from datetime import timedelta

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:login"))

    return render(request, "order/index.html", {
        "categories": Category.objects.all(),
        "restaurants": Restaurant.objects.all(),
        "search": True
    })

def search(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:login"))
    
    if "search" not in request.GET:
        return HttpResponseRedirect(reverse("order:index"))

    search = request.GET["search"].lower()
    words = search.split()

    rests = set()
    for res in Restaurant.objects.all():
        if any(word in res.name.lower().split() for word in words):
            rests.add(res)
    
    for item in Item.objects.all():
        if any(word in item.name.lower().split() for word in words):
            rests.add(item.restaurant)

    return render(request, "order/index.html", {
        "categories": Category.objects.all(),
        "restaurants": rests,
        "searchmessage": f"{len(rests)} restaurants matching '{search}'",
        "search": True
    })

def category(request, slug):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:login"))
    
    try:
        cat = Category.objects.get(slug=slug)
        return render(request, "order/index.html", {
            "categories": Category.objects.all(),
            "category": cat,
            "restaurants": set(item.restaurant for item in cat.items.all()),
            "search": True
        })
    except:
        return render(request, 'order/404.html', status=404)

def menu(request, restaurant, category=None):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:login"))

    try:
        res = Restaurant.objects.get(slug=restaurant)
        if category == None:
            return render(request, "order/menu.html", {
                'restaurant': res
            })
        else:
            cat = Category.objects.get(slug=category)
            return render(request, "order/menu.html", {
                'restaurant': res,
                'category': cat
            })
    except:
        return render(request, 'order/404.html', status=404)

def cart(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:login"))

    if request.method == "POST":
        # Have to fix this major security risk :(
        cart_slug = eval(request.POST['cart'])
        cart = []
        
        for slug, qty in cart_slug.items():
            cart.append({
                'item': Item.objects.get(slug=slug),
                'quantity': qty
            })
        
        # Empty? Handling TODO
        restaurant = cart[0]['item'].restaurant

        return render(request, "order/order.html", {
            "cart": cart,
            "restaurant": restaurant 
        })

    return HttpResponseRedirect(reverse("order:index"))

def order(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:login"))

    if request.method == "POST":
        # Have to fix this major security risk :(
        order_slug = eval(request.POST['order'])
        restaurant_slug = request.POST["restaurant"]

        order = Order.objects.create(user=request.user, restaurant=Restaurant.objects.get(slug=restaurant_slug), placed_at=datetime.datetime.now() + timedelta(hours=5, minutes=30))
        order.save()

        for slug, qty in order_slug.items():
            orderitem = OrderItem.objects.create(order=order, item=Item.objects.get(slug=slug), quantity=qty)
            orderitem.save()
        
        return HttpResponseRedirect(reverse("order:history"))

    return HttpResponseRedirect(reverse("order:index"))

def history(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:login"))
    
    return render(request, 'order/history.html', {
        "orders": Order.objects.filter(user=request.user).order_by('placed_at')
    })