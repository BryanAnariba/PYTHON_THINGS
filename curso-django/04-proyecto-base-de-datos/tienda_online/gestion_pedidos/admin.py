from django.contrib import admin

# Importando modelos para insertar datos desde el panel de django
from gestion_pedidos.models import Client, Article, Order

# Si quieres que un campo sea nulo debes hacer 
    #email = models.EmailField(blank=True, null=True)
class ClientsAdmin(admin.ModelAdmin):
    list_display=("firstName", "lastName", "address", "email", "phone")
    search_fields=["firstName", "lastName", "email"]

class ArticlesAdmin(admin.ModelAdmin):
    list_display=("articleName", "articleSection", "articlePrice")
    search_fields=["articlePrice"]

class OrdersAdmin(admin.ModelAdmin):
    list_display=("orderNumber", "orderDate", "orderDelivered")
    list_filter=["orderDate"]

admin.site.register(Client, ClientsAdmin)
admin.site.register(Order, OrdersAdmin)
admin.site.register(Article, ArticlesAdmin)
