from django.contrib import admin
from .models import Produit , Category , Like


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'price_reduction', 'available', 'created_at']
    list_filter = ['price_reduction' , 'available' , 'created_at' , 'updated_at']
    list_editable = ['available']
    prepopulated_fields = {'slug': ('title',)}

class LikeAdmin(admin.ModelAdmin):
    list_display = ['user', 'produit' , 'created_at']
   

admin.site.register(Category , CategoryAdmin)
admin.site.register(Produit , ProductAdmin)
admin.site.register(Like , LikeAdmin)