from rest_framework import serializers
from .models import producto

class ProductoSerializer(serializers.ModelSerializer):
    """
    ProductoSerializer es un serializador para el modelo Producto.
    Este serializador convierte instancias del modelo Producto a representaciones JSON y viceversa.
    Atributos:
        Meta (class): Clase anidada que define la configuración del serializador.
            - model (Producto): El modelo que se va a serializar.
            - fields (list): Lista de campos del modelo que se incluirán en la representación JSON.
            - read_only_fields (list): Lista de campos que serán de solo lectura.
    Campos serializados:
        - id (int): Identificador único del producto (solo lectura).
        - nombre (str): Nombre del producto.
        - categoria (str): Categoría a la que pertenece el producto.
        - precio (float): Precio del producto.
        - descripcion (str): Descripción del producto.
    """
    class Meta:
        model = producto
        fields = ['id', 'nombre', 'categoria', 'precio', 'descripcion']
        read_only_fields = ['id']