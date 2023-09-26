from django.contrib import admin

from main.models import Dish, Worker, OrderDish, Order

admin.site.register(Dish)
admin.site.register(Worker)
admin.site.register(Order)
admin.site.register(OrderDish)
