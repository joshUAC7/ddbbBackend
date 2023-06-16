from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from uuid import uuid4

# Create your models here.
class CustomUserModelManager(BaseUserManager):
  def create_user(self, username, email,razonSocial,dni,telefono, password=None):
    """
      Creates a custom user with the given fields
    """

    user = self.model(
      username = username,
      email = self.normalize_email(email),
      razonSocial=razonSocial,
      dni=dni,
      telefono=telefono
    )


    user.set_password(password)
    user.save(using = self._db)

    return user

  
  def create_superuser(self, username, email, password):
    user = self.create_user(
      username,
      email,
      password = password,
      razonSocial="vago",
      dni="76988554",
      telefono="987654123"
    )

    user.is_staff = True
    user.is_superuser = True
    user.save(using = self._db)

    return user


class CustomUserModel(AbstractBaseUser, PermissionsMixin):
    userId    = models.CharField(max_length = 16, default = uuid4().hex[:15], primary_key = True, editable = False)
    username  = models.CharField(max_length = 16, unique = True, null = False, blank = False)
    email     = models.EmailField(max_length = 100, unique = True, null = False, blank = False)
    razonSocial  = models.CharField(max_length = 30)
    dni  = models.CharField(max_length = 8)
    direccion  =models.CharField(max_length = 100)
    telefono  = models.CharField(max_length = 9)
    genero  = models.CharField(max_length = 1)

    USERNAME_FIELD = "username"
    # REQUIRED_FIELDS = ["email","razonSocial","dni","direccion","telefono","genero"]
    REQUIRED_FIELDS = ["email"]

    active       = models.BooleanField(default = True)

    is_staff     = models.BooleanField(default = False)
    is_superuser = models.BooleanField(default = False)

    created_on   = models.DateTimeField(auto_now_add = True, blank = True, null = True)
    updated_at   = models.DateTimeField(auto_now = True)

    objects = CustomUserModelManager()

    def __str__(self):
        return self.username + "," + self.email
    def has_perm(self,perm,obj=None):
        return self.is_admin
    def has_module_perms(self,app_label):
        return True
    class Meta:
        verbose_name = "Custom User"
