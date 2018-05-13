# Python imports


# Django imports
from django.conf import settings
from django.core.mail import send_mail


# Third party apps imports
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


# Local imports


# Create your viewsets here.
class ContactEmail(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request, *args, **kwargs):
        subject = "{0} {1}".format(
            "[Contacto]", request.data["nombres_apellidos"])
        send_mail(
            subject,
            "Nombres y Apellidos: {0}\nEmail: {1}\nTelefono: {2}\n".format(
                request.data["nombres_apellidos"], request.data["email"],
                request.data["telefono"]) +
            "Mensaje: {0}".format(request.data["mensaje"]),
            settings.EMAIL_HOST_USER,
            ["ventas@bioserviceclab.com"],
            fail_silently=False)
        return Response({}, status=status.HTTP_200_OK)


class DistributorEmail(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request, *args, **kwargs):
        subject = "{0} {1}".format("[Distribuidor]", request.data["email"])
        send_mail(
            subject,
            "Razon Social: {0}\nRuc: {1}\nDireccion: {2}\n".format(
                request.data["razon_social"], request.data["ruc"],
                request.data["direccion"]) +
            "Telefono: {0}\nEmail: {1}\nMensaje: {2}".format(
                request.data["telefono"], request.data["email"],
                request.data["mensaje"]),
            settings.EMAIL_HOST_USER,
            ["ventas@bioserviceclab.com"],
            fail_silently=False)
        return Response({}, status=status.HTTP_200_OK)
