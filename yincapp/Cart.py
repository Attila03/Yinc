
from .models import Product, ProductCount


'''
SessionCart = {
    "id": {"count": 2, "name": name, "price": price of single object},
    ...
}
'''


def cart_add(request, cart, idx):
    if idx in cart:
        cart[idx]["count"] += 1
    else:
        item = Product.objects.get(pk=int(idx))
        cart[idx] = {"count": 1, "name": item.name, "price": item.price}
    request.session["total"] += cart[idx]["price"]
    request.session.modified = True


def cart_sub(request, cart, idx):
    if cart[idx]["count"] > 1:
        cart[idx]["count"] -= 1
        request.session["total"] -= Product.objects.get(pk=int(idx)).price
        request.session.modified = True


def cart_remove(request, cart, idx):
    request.session["total"] -= cart[idx]["count"]*cart[idx]["price"]
    cart.pop(idx)
    request.session.modified = True


def sessioncart_to_dbcart(request, sessioncart, dbcart):

    item_indices = [int(x) for x in sessioncart.keys()]

    items = Product.objects.filter(id__in=item_indices)
    for item in items:
        ProductCount(product=item, cart=dbcart, count=sessioncart[str(item.id)]["count"]).save()

