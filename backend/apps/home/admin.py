from django.contrib import admin
from .models import Product, Category, Image, ProductFeature


# Register your models here.
class ImageInline(admin.TabularInline):
    model = Image
    extra = 0


class FeatureInline(admin.TabularInline):
    model = ProductFeature
    extra = 0


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    raw_id_fields = ["category"]
    list_display = ["name", "inventory", "new_price", "create_at", "modify_at"]
    prepopulated_fields = {"slug": ("name",)}
    list_filter = ["create_at", "modify_at"]
    inlines = [ImageInline, FeatureInline]
