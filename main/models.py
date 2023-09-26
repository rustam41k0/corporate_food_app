from django.db import models


class Worker(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Dish(models.Model):
    title = models.CharField(max_length=150)
    composition = models.CharField(max_length=150)
    price = models.IntegerField()

    def __str__(self):
        return self.title


class Order(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    worker = models.ForeignKey('Worker', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.worker.name}'s {self.id} order"


class OrderDish(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE, related_name='dish')
    dish = models.ForeignKey('Dish', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.dish.title}'
