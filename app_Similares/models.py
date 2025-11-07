from django.db import models

# ==========================================
# MODELO: Cliente
# ==========================================
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=200)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    registrado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

# ==========================================

# MODELO: Medicamento
# ==========================================
class Medicamento(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField()
    laboratorio = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    fecha_vencimiento = models.DateField()
    codigo_barras = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre

# ==========================================
# MODELO: Venta
# ==========================================
class Venta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='ventas')  # 1 a muchos
    medicamentos = models.ManyToManyField(Medicamento, related_name='ventas')  # muchos a muchos
    fecha_venta = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    metodo_pago = models.CharField(max_length=50, choices=[
        ('EFECTIVO', 'Efectivo'),
        ('TARJETA', 'Tarjeta'),
        ('TRANSFERENCIA', 'Transferencia'),
    ])
    numero_factura = models.CharField(max_length=20, unique=True)
    observaciones = models.TextField(blank=True, null=True)
    estado = models.CharField(max_length=20, default='COMPLETADA', choices=[
        ('COMPLETADA', 'Completada'),
        ('PENDIENTE', 'Pendiente'),
        ('CANCELADA', 'Cancelada'),
    ])

    def __str__(self):
        return f"Venta {self.numero_factura} - {self.cliente.nombre}"