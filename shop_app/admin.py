from django.contrib import admin
from shop_app.models import CategoryProduct, Product, UserCart


@admin.register(CategoryProduct)
class CategoryAdminModel(admin.ModelAdmin):
    search_fields = ['category_name', 'id', 'created_at']
    list_filter = ['created_at']
    list_display = ['id', 'category_name', 'created_at']
    ordering = ['-id']


@admin.register(Product)
class ProductAdminModel(admin.ModelAdmin):
    search_fields = ['id', 'product_name', 'product_category']
    list_filter = ['created_at']
    list_display = ['id', 'product_name', 'product_cost', 'product_count', 'product_category']
    ordering = ['-id']


@admin.register(UserCart)
class UserCartAdminModel(admin.ModelAdmin):
    search_fields = ['id', 'product', 'product_count']
    list_filter = ['created_at']
    list_display = ['id', 'product', 'product_count']
    ordering = ['-id']
    