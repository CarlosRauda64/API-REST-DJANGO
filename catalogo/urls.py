from rest_framework import routers
from catalogo.api import ProductoViewSet, UsuarioViewSet

router = routers.DefaultRouter()

router.register('api/productos', ProductoViewSet, 'productos')
router.register('api/usuarios', UsuarioViewSet, 'usuarios')

urlpatterns = router.urls