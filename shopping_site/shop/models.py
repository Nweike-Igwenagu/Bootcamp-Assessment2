from django.db import models

# Create your models here.
model_choices = [('Tshirts', 'Tshirts'),
                ('Pants', 'Pants'),
                ('Shorts', 'Shorts'),
                ]

order_status = [('Susessful', 'Susessful'),
                ('Pending', 'Pending'),
                ('Failed', 'Failed'),
                ]

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    model = models.CharField(max_length=50, choices = model_choices)
    description = models.CharField(max_length=225)
    
    def __str__(self):
        return self.name
    
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default=1)

    @property
    def total_price(self):
        return self.product.price * self.quantity
    
    def __str__(self):
        return f"{self.quantity} {self.product} ordered on {self.order_date}"