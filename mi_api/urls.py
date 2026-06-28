from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'usuarios', views.UsuariosViewSet)
router.register(r'zonas', views.ZonasViewSet)
router.register(r'tipo-falla', views.TipoFallaViewSet)
router.register(r'tickets', views.TicketViewSet)
router.register(r'adjuntos', views.AdjuntoViewSet)
router.register(r'bitacoras', views.BitacoraTicketViewSet)
router.register(r'bitacora-adjuntos', views.BitacoraAdjuntosViewSet)

urlpatterns = [
    path('', include(router.urls)),
]