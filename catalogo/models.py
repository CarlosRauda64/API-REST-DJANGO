from django.db import models

# Create your models here.
class producto(models.Model):
    """
    Clase que representa un producto en el catálogo.

    Atributos:
        nombre (CharField): Nombre del producto, con un máximo de 50 caracteres.
        categoria (CharField): Categoría a la que pertenece el producto, con un máximo de 50 caracteres.
        precio (DecimalField): Precio del producto.
        descripcion (TextField): Descripción detallada del producto.
    """
    nombre = models.CharField(max_length=50)
    categoria = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField()