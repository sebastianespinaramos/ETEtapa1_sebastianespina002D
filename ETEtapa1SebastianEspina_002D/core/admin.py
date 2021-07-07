from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from .models import usuario, Marca, Producto
# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "precio", "nuevo", "marca"]
    list_editable = ["precio"]
    search_fields = ["nombre"]
    list_filter = ["marca", "nuevo"]
    list_per_page = 5

admin.site.register(usuario)
admin.site.register(Marca)
admin.site.register(Producto, ProductoAdmin)


