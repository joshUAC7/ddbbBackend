from django.db import models

# Create your models here.

class Evento(models.Model):
    nombre = models.CharField(max_length=50)
    img = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=300)
    catering = models.BooleanField(default=True)
    def __str__(self):
        return str(self.nombre)

class Reserva(models.Model):
    fecha = models.DateField(null=False)
    costo = models.DecimalField(max_digits=8,decimal_places=2,null=False)
    descuento = models.IntegerField(null=False,default=0)
    lugar = models.CharField(max_length =100,null=False)
    cliente = models.ForeignKey('drfauth.CustomUserModel',on_delete=models.CASCADE)
    evento = models.ForeignKey(Evento,on_delete=models.CASCADE)


class Pago(models.Model):
    tipoPago = models.CharField(max_length=50)
    fechaInicial = models.DateField(null=False)
    estado = models.BooleanField(default=False)
    monto = models.DecimalField(max_digits=8,decimal_places=2,null=False)
    reserva = models.ForeignKey(Reserva,on_delete=models.CASCADE)

class DetalleReserva(models.Model):
    cantidadPersonal = models.IntegerField(null=False,default=0)
    cantidadInvitados = models.IntegerField(null=False,default=0)
    cantidadMesas = models.IntegerField(null=False,default=0)
    reserva = models.OneToOneField(Reserva,on_delete=models.CASCADE,primary_key=True)


