from rest_framework import routers
from .api import ColoresViewSet, PublicacionesViewSet, PersonalizacionesViewSet, UsuarioViewSet, CarrosViewSet


router = routers.DefaultRouter()


router.register('api/colores', ColoresViewSet, 'colores')
router.register('api/publicaciones', PublicacionesViewSet, 'publicaciones')
router.register('api/personalizaciones', PersonalizacionesViewSet, 'personalizaciones')
router.register('api/usuario', UsuarioViewSet, 'usuario')
router.register('api/carros', CarrosViewSet, 'carros')

urlpatterns = router.urls