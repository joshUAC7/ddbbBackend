from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from logic.models import DetalleReserva, Evento, Pago,Reserva

class EventoModelSerializer(ModelSerializer):
    class Meta:
        model = Evento
        fields = [
           "id",
          "nombre",
          "img",
          "descripcion",
          "catering"
        ]


class DetalleReservaModelSerializer(ModelSerializer):
    class Meta:
        model=DetalleReserva
        fields = [
          "cantidadPersonal",
          "cantidadInvitados",
          "cantidadMesas",
        ]
class PagoModelSerializer(ModelSerializer):
    class Meta:
        model=Pago
        fields = [
          "tipoPago",
          "fechaInicial",
          "estado",
          "monto"
        ]
class ReservaModelSerializer(ModelSerializer):
    evento = EventoModelSerializer()
    class Meta:
        model = Reserva
        fields = [
           "id",
          "fecha",
          "costo",
          "descuento",
          "lugar",
          "evento",
        ]


