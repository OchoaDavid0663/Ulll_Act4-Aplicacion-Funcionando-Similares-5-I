from django.contrib import admin
from .models import Cliente, Medicamento, Venta

# Registra tus modelos aquí.
admin.site.register(Cliente)
admin.site.register(Medicamento) # ¡Asegúrate de que esta línea esté presente!
admin.site.register(Venta)