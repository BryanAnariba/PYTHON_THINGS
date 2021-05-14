from django.contrib import admin

# Importando modelos para insertar datos desde el panel de django
from gestion_pedidos.models import Client, Article, Order

# Si quieres que un campo sea nulo debes hacer 
    #email = models.EmailField(blank=True, null=True)

admin.site.register(Client)
admin.site.register(Order)
admin.site.register(Article)
