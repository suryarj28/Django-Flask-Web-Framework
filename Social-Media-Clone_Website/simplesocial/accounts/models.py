from django.db import models
from django.contrib.auth.models import User as Users, PermissionsMixin
from django.utils import timezone


# Create your models here.

class User(Users, PermissionsMixin):

    def __str__(self):
        return "@{}".format(self.username)
