from django.contrib import admin
from .models import Restaurant, Item, Category
from django.template.defaultfilters import slugify

# Register your models here.
class ItemAdmin(admin.ModelAdmin):
    exclude = ('slug',)

class RestaurantAdmin(admin.ModelAdmin):
    exclude = ('slug',)

class CategoryAdmin(admin.ModelAdmin):
    exclude = ('slug',)

admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Category, CategoryAdmin)