import string
from random import random

import requests
# from allauth.socialaccount.providers import stripe
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views.generic import DetailView, View
from .forms import CheckoutForm
from .models import *


# def create_ref_code():
#     return ''.join(random.choices(string.ascii_lowercase + string.digits, k=20))


def is_valid_form(values):
    valid = True
    for field in values:
        if field == '':
            valid = False
    return valid


@login_required
def add_to_cart(request, slug):
    item = get_object_or_404(Menu, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(item=item, user=request.user, ordered=False)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if item.quantity > 1 :
        if order_qs.exists():
            order = order_qs[0]
            if order.items.filter(item__slug=item.slug).exists():
                order_item.quantity += 1
                order_item.save()
                messages.info(request, "This item quantity was updated to your cart")
                return redirect("order_summary")
            else:
                messages.info(request, "This item was added to your cart")
                order.items.add(order_item)
                return redirect("order_summary")
        else:
            ordered_date = timezone.now()
            order = Order.objects.create(user=request.user, ordered_date=ordered_date)
            order.items.add(order_item)
            messages.info(request, "This item was added to your cart")
            return redirect("order_summary")
    else:
        messages.error(request, "This item was not exist")
        return redirect("/")


@login_required
def remove_from_cart(request, slug):
    item = get_object_or_404(Menu, slug=slug)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(item=item, user=request.user, ordered=False)[0]
            order.items.remove(order_item)
            order_item.delete()
            messages.info(request, "This item was removed to your cart")
            return redirect("order_summary")
        else:
            messages.info(request, "This item was not in your cart")
            return redirect("details_menu", slug=slug)
    else:
        messages.info(request, "You do not have an active item")
        return redirect("details_menu", slug=slug)


class OrderSummaryView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            context = {'object': order}
            return render(self.request, 'order/order_summary.html', context)
        except ObjectDoesNotExist:
            messages.error(self.request, 'You do not have active order')
            return redirect('/')


@login_required
def remove_single_item_from_cart(request, slug):
    item = get_object_or_404(Menu, slug=slug)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(item=item, user=request.user, ordered=False)[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
            else:
                order.items.remove(order_item)
            messages.info(request, "This item quantity was updated to your cart")
            return redirect("order_summary")
        else:
            messages.info(request, "This item was not in your cart")
            return redirect("details_menu", slug=slug)
    else:
        messages.info(request, "You do not have an active item")
        return redirect("details_menu", slug=slug)


class CheckoutView(View):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            form = CheckoutForm()
            context = {'form': form, 'order': order}
            address_qs = Address.objects.filter(user=self.request.user, default=True)
            if address_qs.exists():
                context.update({'default_address': address_qs[0]})
            return render(self.request, 'order/checkout.html', context)
        except ObjectDoesNotExist:
            messages.error(self.request, 'You do not have active order')
            return redirect('checkout')

    def post(self, *args, **kwargs):
        form = CheckoutForm(self.request.POST or None)
        print('0')
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            print('1')
            if form.is_valid():
                print('2')
                order_items = order.items.all()
                order_items.update(ordered=True)
                for item in order_items:
                    item.save()
                use_default = form.cleaned_data.get('use_default')
                if use_default:
                    print('3')
                    address_qs = Address.objects.filter(user=self.request.user, default=True)
                    if address_qs.exists():
                        print('4')
                        address = address_qs[0]
                        order.address = address
                        order.save()
                    else:
                        print('5')
                        messages.info(
                            self.request, "No default address available")
                        return redirect('core:checkout')
                else:
                    print('6')
                    address = form.cleaned_data.get('address')
                    city = form.cleaned_data.get('city')
                    zip = form.cleaned_data.get('zip')
                    # same_profile_address = form.cleaned_data.get('same_profile_address')
                    # save_info = form.cleaned_data.get('save_info')
                    if is_valid_form([address, city, zip]):
                        print('7')
                        address = Address(
                            user=self.request.user,
                            address=address,
                            city=city,
                            zip=zip)
                        address.save()
                        order.address = address
                        # order.items.item.quantity = int(order.items.item.quantity) - order.items.quantity
                        order.ordered = True
                        # order.ref_code = create_ref_code()
                        order.save()
                        set_default = form.cleaned_data.get(
                            'set_default_shipping')
                        if set_default:
                            print('8')
                            address.default = True
                            address.save()
                        # order.items.item.quantity.save()
                        messages.success(self.request, 'Your order was successfully')
                        return redirect('/')
                    else:
                        print('9')
                        messages.info(
                            self.request, "Please fill in the required shipping address fields")

            else:
                print('10')
                messages.warning(self.request, 'Failed checkout!')
                return redirect('checkout')
        except ObjectDoesNotExist:
            messages.error(self.request, 'You do not have active order')
            return redirect('/')


def history_orders(request):
    re = Order.objects.filter(user=request.user)
    context = {
        'object_list': re,
    }
    return render(request, 'order/history_orders.html', context)


def orders(request):
    re = OrderItem.objects.filter(item__branch__manager=request.user)
    context = {
        'object_list': re,
    }
    return render(request, 'order/orders.html', context)


