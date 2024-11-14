from .models import producto, usuario
from rest_framework import viewsets, permissions
from .serializers import ProductoSerializer, UsuarioSerializer
from django_filters.rest_framework import DjangoFilterBackend

class ProductoViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite a los productos ser vistos o editados.
    """
    queryset = producto.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductoSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite a los usuarios ser vistos o editados.
    """
    queryset = usuario.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UsuarioSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['correo']
    filterset_fields = ['contrasena']
    