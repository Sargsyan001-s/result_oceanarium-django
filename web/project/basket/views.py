from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from products_app.models import Product, Order, Pos_order
from .basket import Basket
from .forms import BasketAddProductForm, OrderForm


def basket_detail(request):
    basket = Basket(request)
    return render(request, 'basket/detail.html', {'basket': basket})


def basket_remove(request, product_id):
    basket = Basket(request)
    product = get_object_or_404(Product, pk=product_id)
    basket.remove(product)
    return redirect('basket_detail')


def basket_clear(request):
    basket = Basket(request)
    basket.clear()
    return redirect('basket_detail')


@require_POST
def basket_add(request, product_id):
    basket = Basket(request)
    product = get_object_or_404(Product, pk=product_id)
    form = BasketAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        basket.add(
            product=product,
            count=cd['count'],
            update_count=cd['reload']
        )
    return redirect('basket_detail')


@login_required
def open_order(request):
    context = {
        'form_order': OrderForm()
    }
    return render(request, 'basket/order/order_form.html', context)


@login_required
def basket_buy(request):
    basket = Basket(request)

    if len(basket) <= 0:
        return redirect('product_list')

    if request.method == 'POST':
        form_order = OrderForm(request.POST)
        if form_order.is_valid():
            order = form_order.save(commit=False)
            order.user = request.user
            order.price = float(basket.get_total_price())
            order.save()

            for item in basket:
                Pos_order.objects.create(
                    product=item['product'],
                    order=order,
                    count=item['count']
                )

            basket.clear()
            return redirect('my_orders')

    return redirect('order_open')


@login_required
def my_orders(request):
    order_list = Order.objects.filter(user=request.user).order_by('-date_create')
    return render(request, 'basket/my_orders.html', {'order_list': order_list})
