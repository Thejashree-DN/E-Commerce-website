from django.shortcuts import render, get_object_or_404, redirect
from products.models import Product
from .models import Cart, CartItem

def cart_detail(request):
    cart, created = Cart.objects.get_or_create(id=request.session.get("cart_id"))
    request.session["cart_id"] = cart.id
    return render(request, "cart/cart_detail.html", {"cart": cart})

def add_to_cart(request, product_id):
    cart, created = Cart.objects.get_or_create(id=request.session.get("cart_id"))
    request.session["cart_id"] = cart.id
    product = get_object_or_404(Product, id=product_id)
    item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        item.quantity += 1
    item.save()
    return redirect("cart:cart_detail")
