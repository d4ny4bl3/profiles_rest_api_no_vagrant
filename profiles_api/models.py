from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionMixin


class UserProfile(AbstractBaseUser, PermissionMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
