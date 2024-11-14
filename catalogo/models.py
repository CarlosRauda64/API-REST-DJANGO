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

class usuario(models.Model):
    """
    Clase que representa un usuario en el sistema.

    Atributos:
        nombre (CharField): Nombre del usuario, con un máximo de 50 caracteres.
        correo (EmailField): Correo electrónico del usuario.
        contrasena (CharField): Contraseña del usuario, con un máximo de 50 caracteres.
    """
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    contrasena = models.CharField(max_length=50)
    rol = models.CharField(max_length=50)