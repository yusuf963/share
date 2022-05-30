from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from .utility.city_selection import city_selection

class MyUserManager(BaseUserManager):
    def create_user(self, email,username,first_name,last_name, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
        )

        user.set_password(password)
        # user.set_unusable_password()
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, first_name, last_name, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email= self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser,PermissionsMixin):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    city = models.CharField(max_length=50, choices=city_selection, null=True, blank=True, default='LOND')
    personal_photo = models.ImageField(upload_to='share/photos/users/%Y/%m/%d/',null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    postcode = models.CharField(max_length=10, null=True, blank=True)
    door_number = models.CharField(max_length=10, null=True, blank=True)
    latitude = models.CharField(max_length=20,null=True, blank=True)
    longitude = models.CharField(max_length=20,null=True, blank=True)
    reduced_carbon_emission = models.FloatField(default=0)
# REQUIRED_FIELDS FOR the default USER MODEL
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

# make email is the required field to login
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name','last_name']
    
# Tell this class to use our custom User Manager
    objects = MyUserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    # def get_full_name(self):
    #     return self.username

    # def get_short_name(self):
    #     return self.username