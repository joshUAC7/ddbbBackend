from dj_rest_auth.views import AllowAny,IsAuthenticated
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework.response import Response

from .serializers import DetalleReservaModelSerializer, EventoModelSerializer, PagoModelSerializer, ReservaModelSerializer
from .models import DetalleReserva, Evento, Pago,Reserva
# Create your views here.

class EventosApi(APIView):
    permission_classes= [AllowAny]
    def get(self,request):
        myEvents = Evento.objects.all()
        serializer = EventoModelSerializer(myEvents,many=True)
        return JsonResponse(serializer.data,safe=False)

class Content(APIView):
    permission_classes= [IsAuthenticated]
    def get(self,request,*args,**kwargs):
        reservas = Reserva.objects.filter(cliente_id=request.user.userId)
        # reservas = Reserva.objects.all()
        data = []
        for i in reservas:
            detalleReserva = DetalleReserva.objects.get(reserva_id=i.id)
            serDetalleReserva = DetalleReservaModelSerializer(detalleReserva)
            serReserva = ReservaModelSerializer(i)
            pago = Pago.objects.filter(reserva_id=i.id)
            serPago = PagoModelSerializer(pago,many=True)
            data.append({**serReserva.data,**serDetalleReserva.data,"pago":serPago.data})
        print(data)
        # detalleReserva = [DetalleReserva.objects.get(reserva_id=i.id) for i in reservas]
        # print(detalleReserva)
        # myPagos = [Pago.objects.filter(reserva_id=i.id) for i in reservas]
        myEvents = Evento.objects.all()
        serializerEvents = EventoModelSerializer(myEvents,many=True)
        # serializerPagos = PagoModelSerializer(myPagos,many=True)

        return JsonResponse({"Reservas":data,"Eventos":serializerEvents.data},safe=False)

class ReservaAPIGeneric(generics.GenericAPIView,mixins.CreateModelMixin):
    permission_classes=[IsAuthenticated]
    serializer_class=ReservaModelSerializer
    queryset = Reserva.objects.all()
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
class DetalleReservaAPIGeneric(generics.GenericAPIView,mixins.CreateModelMixin):
    permission_classes=[IsAuthenticated]
    serializer_class=DetalleReservaModelSerializer
    queryset = DetalleReserva.objects.all()
    def post(self,request):
        self.create(request)

class PagoAPIGeneric(generics.GenericAPIView,mixins.CreateModelMixin):
    serializer_class=Pago
    queryset = Pago.objects.all()
    # def get(self,request):
        # return self.list(request)
    def post(self,request):
        self.create(request)

