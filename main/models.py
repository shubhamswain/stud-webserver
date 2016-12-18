from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class MyUserManager(BaseUserManager):
    def create_user(self, webmail, password=None):
        """
        Creates and saves a User with the given webmail and password.
        """
        if not webmail:
            raise ValueError('Users must have an webmail address')

        user = self.model(webmail=(webmail))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, webmail, password):
        """
        Creates and saves a superuser with the given webmail and password.
        """
        user = self.create_user(webmail, password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):

    webmail = models.CharField(verbose_name='Webmail', max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'webmail'
    REQUIRED_FIELDS = []

    def get_full_name(self):
        # The user is identified by their webmail address
        return self.webmail

    def get_short_name(self):
        # The user is identified by their webmail address
        return self.webmail

    def __str__(self):              # __unicode__ on Python 2
        return self.webmail
        
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
