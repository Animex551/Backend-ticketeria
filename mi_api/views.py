from rest_framework import viewsets
from .models import Usuarios, Zonas, TipoFalla, Tickets, Adjunto, BitacoraTicket, BitacoraAdjuntos
from .serializers import *

class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = Usuarios.objects.all()
    serializer_class = UsuariosSerializer

class ZonasViewSet(viewsets.ModelViewSet):
    queryset = Zonas.objects.all()
    serializer_class = ZonasSerializer

class TipoFallaViewSet(viewsets.ModelViewSet):
    queryset = TipoFalla.objects.all()
    serializer_class = TipoFallaSerializer

class TicketViewSet(viewsets.ModelViewSet):
    queryset = Tickets.objects.all().order_by('-fecha_creacion')
    serializer_class = TicketSerializer

class AdjuntoViewSet(viewsets.ModelViewSet):
    queryset = Adjunto.objects.all()
    serializer_class = AdjuntoSerializer

class BitacoraTicketViewSet(viewsets.ModelViewSet):
    queryset = BitacoraTicket.objects.all().order_by('-fecha_registro')
    serializer_class = BitacoraTicketSerializer

class BitacoraAdjuntosViewSet(viewsets.ModelViewSet):
    queryset = BitacoraAdjuntos.objects.all()
    serializer_class = BitacoraAdjuntosSerializer