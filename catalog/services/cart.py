from django.contrib.auth.models import User
from catalog.models import Order, Order_Dish, Dish

def dish_count(user: User, dish: Dish):
    if user.is_authenticated:
        order = Order.objects.filter(user=user, status=Order.statuses.not_started).first()
        if order:
            order_dish = Order_Dish.objects.filter(order=order, dish=dish).first()
            if order_dish:
                return order_dish.count
    return 0

def plus_to_cart(user: User, dish: Dish):
    order = Order.objects.get_or_create(
            user=user,
            status=Order.statuses.not_started,
            defaults={
                'time': None,
                })[0]
    if order:
        order_dish = Order_Dish.objects.filter(order=order.id, dish=dish.id).first()
        if order_dish:
            order_dish.count += 1
            order_dish.save()
        else:
            Order_Dish.objects.create(dish=dish, order=order, count=1)
    else:
        raise ValueError('Can not create order')

def minus_to_cart(user: User, dish: Dish):
    try:
        order = Order.objects.get(
                user=user,
                status=Order.statuses.not_started,
                )
    except:
        return
    order_dish = Order_Dish.objects.filter(order=order.id, dish=dish.id).first()
    if order_dish:
        if order_dish.count == 1:
            order_dish.delete()
        else:
            order_dish.count -= 1
            order_dish.save()

def remove_from_cart(user: User, dish: Dish):
    try:
        order = Order.objects.get(
                user=user,
                status=Order.statuses.not_started,
                )
    except:
        return
    order_dish = Order_Dish.objects.filter(order=order.id, dish=dish.id).first()
    if order_dish:
        order_dish.delete()
    return
