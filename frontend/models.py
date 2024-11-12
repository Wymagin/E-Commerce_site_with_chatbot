from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User

class Category(models.Model):

    class Meta:
        verbose_name_plural = "Categories"
    name = models.CharField(max_length=200, blank=False)
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200, blank=False)
    price = models.IntegerField(default=0, blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True)
    description = models.TextField(max_length=600, blank=False, default='---')
    image = models.ImageField(null=True, default='default.jpg', blank=True)
    stock = models.IntegerField(default=0, blank=False)
    tags = TaggableManager()

    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart {self.id} for {self.user}"

    @property
    def total_price(self):
        return sum(item.total_price for item in self.items.all())


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_price(self):
        return self.quantity * self.product.price

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"