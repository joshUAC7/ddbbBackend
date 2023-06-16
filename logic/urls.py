
from django.urls import path,include
from .views import Content, DetalleReservaAPIGeneric, ReservaAPIGeneric,EventosApi
urlpatterns = [
    # path("user/", UserApiView.as_view(), name="rest_user_details"),
    path("reservar/",ReservaAPIGeneric.as_view(),name="add Reserva"),
    path("detalleReservar/",DetalleReservaAPIGeneric.as_view(),name="add DetalleReserva"),
    path("eventos/",EventosApi.as_view(),name="eventos"),
    path("content/",Content.as_view())
    # path("pago/")
        ]
