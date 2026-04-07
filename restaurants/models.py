from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.template.defaultfilters import slugify

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=64)
    picture = models.ImageField(upload_to='images/categories/')

    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

class Restaurant(models.Model):
    name = models.CharField(max_length=64)
    address = models.CharField(max_length=512)
    rating = models.FloatField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    numRatings = models.IntegerField(default=0)

    slug = models.SlugField(unique=True)

    picture = models.ImageField(upload_to='images/restaurants/')

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

class Item(models.Model):
    name = models.CharField(max_length=64)
    picture = models.ImageField(upload_to=f'images/items/')
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    veg = models.BooleanField(default=False)

    # Have to change on delete
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="items")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="items", null=True)

    is_available = models.BooleanField(default=False)

    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name + f" ({self.restaurant})"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)