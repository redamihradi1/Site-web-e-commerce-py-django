from django.contrib import admin

from .models import Category, Product



admin.site.site_header=' * Gaming Store * Administration'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name', 'slug']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','category', 'author', 'slug', 'price',
                    'in_stock', 'created', 'updated']
    list_filter = ['in_stock', 'is_active' ,'category']
    list_editable = ['price', 'in_stock' ]
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'author', 'slug', 'price']

