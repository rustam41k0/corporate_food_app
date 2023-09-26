from django.forms import formset_factory
from .models import Order, OrderDish
from django import forms


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['worker']


class OrderDishForm(forms.ModelForm):
    class Meta:
        model = OrderDish
        fields = ['dish']


OrderDishFormSet = formset_factory(OrderDishForm, extra=10)
