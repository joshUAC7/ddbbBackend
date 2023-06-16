from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import CustomUserModel
from django.conf import settings

class CustomUserModelSerializer(ModelSerializer):
  class Meta:
    model = CustomUserModel
    fields = [
      "userId",
      "username",
      "password",
"email","razonSocial","dni","direccion","telefono","genero"
    ]

  def create(self, validated_data):
    user = CustomUserModel.objects.create_user(
      validated_data["username"],
      validated_data["email"],
      validated_data["password"]
    )

    return user


class CustomRegisterSerializer(RegisterSerializer):
    razonSocial = serializers.CharField(required=True)
    dni = serializers.CharField(required=True)
    direccion = serializers.CharField(required=True)
    telefono = serializers.CharField(required=True)
    genero = serializers.CharField(required=True)
    def get_cleaned_data(self):
        super(CustomRegisterSerializer,self).get_cleaned_data()
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
            'razonSocial': self.validated_data.get('razonSocial',''),
            'dni': self.validated_data.get('dni',''),
            'direccion': self.validated_data.get('direccion',''),
            'telefono': self.validated_data.get('telefono',''),
            'genero': self.validated_data.get('genero',''),
                }
    
