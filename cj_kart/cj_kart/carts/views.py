from django.shortcuts import render,redirect
from mainapp.models import Products
from .models import Carts,Cart_items
# Create your views here.


def Cart_view(request): #this function is for view Cart page
    return render(request,'mainapp/cart.html')

def _cart_id(request): #this private function is using to fetch the session id of a single product
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


def add_to_cart(request,product_id): #to get the Product
    product = Products.objects.get(id=product_id)
    try:
        cart = Carts.objects.get(cart_id=_cart_id(request)) #get the cart id using the cart session
    except Carts.DoesNotExist:
        cart = Carts.objects.create(
            cart_id = _cart_id(request)
        )
    cart.save()

    try:
        cart_item = Cart_items.objects.get(product=product,cart=cart) #if there is morethan one time add to a single product in cart the qty will incresse
        cart_item.quantity += 1 #expantion -> (cart_item.quantity = cart_item.quantity + 1)
        cart_item.save()

    except Cart_items.DoesNotExist: #if there is no Existing product here then add the product to the cart
        cart_item = Cart_items.objects.create(
            product = product,
            quantity = 1,
            cart = cart,
        )
        cart_item.save()
    return redirect('cart')