from .models import producto
from rest_framework import viewsets, permissions
from .serializers import ProductoSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite a los productos ser vistos o editados.
    """
    queryset = producto.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductoSerializer
    