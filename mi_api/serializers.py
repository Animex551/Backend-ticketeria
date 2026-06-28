from rest_framework import serializers
from .models import Usuarios, Zonas, TipoFalla, Tickets, Adjunto, BitacoraTicket, BitacoraAdjuntos

class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = ['email', 'username', 'is_IT', 'is_admin'] # Excluimos password por seguridad en las respuestas

class ZonasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zonas
        fields = '__all__'

class TipoFallaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoFalla
        fields = '__all__'

class TicketSerializer(serializers.ModelSerializer):
    # Esto te permite incluir opcionalmente los detalles anidados si React los necesita leer,
    # o simplemente usar los IDs para crear/actualizar.
    class Meta:
        model = Tickets
        fields = '__all__'

class AdjuntoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adjunto
        fields = '__all__'

class BitacoraTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = BitacoraTicket
        fields = '__all__'

class BitacoraAdjuntosSerializer(serializers.ModelSerializer):
    class Meta:
        model = BitacoraAdjuntos
        fields = '__all__'