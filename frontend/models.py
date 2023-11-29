from django.db import models
from taggit.managers import TaggableManager



# class Category(models.Model):
#     name = models.CharField(max_length=255, db_index=True)
#     friendly_name = models.CharField(max_length=200, null=True, blank=True)
#
#     def __str__(self):
#         return self.name
#
#     def get_friendly_name(self):
#         return self.friendly_name

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
    description = models.TextField(max_length=600, blank=False, default='uwu')
    image = models.ImageField(null=True, default='default.jpg', blank=True)
    stock = models.IntegerField(default=0, blank=False)
    tags = TaggableManager()

    def __str__(self):
        return self.name


# Create your models here.
