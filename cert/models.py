from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager
)
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def create_user(self, user_id, email, call_sign, name, password=None):
        if not user_id:
            raise ValueError("User must have a user id")
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")
        if not name:
            raise ValueError("User must have a name")

        user = self.model(
            email=self.normalize_email(email)
        )

        user.user_id = user_id
        user.name = name
        user.call_sign = call_sign
        user.set_password(password)  # change password to hash
        user.is_admin = False
        user.is_staff = False
        user.save(using=self._db)
        return user

    def create_staffuser(self, user_id, email, name, call_sign, password=None):
        if not user_id:
            raise ValueError("User must have a user id")
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")
        if not name:
            raise ValueError("User must have a name")

        user = self.model(
            email=self.normalize_email(email)
        )
        user.user_id = user_id
        user.name = name
        user.call_sign = call_sign
        user.set_password(password)  # change password to hash
        user.is_admin = False
        user.is_staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, user_id, email, name, call_sign, password=None):
        if not user_id:
            raise ValueError("User must have a user id")
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")
        if not name:
            raise ValueError("User must have a name")

        user = self.model(
            email=self.normalize_email(email)
        )
        user.user_id = user_id
        user.name = name
        user.call_sign = call_sign
        user.set_password(password)  # change password to hash
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser):
    user_id = models.CharField(_('?????????'), max_length=50, unique=True)
    email = models.EmailField(_('?????????'), unique=True)
    name = models.CharField(_('??????'), max_length=60)
    call_sign = models.CharField(_('?????????'), max_length=60, unique=True)
    profile_image = models.ImageField(_('???????????????'), blank=True, upload_to='profiles', default='profiles/default.png')
    is_active = models.BooleanField(_('?????? ???????????????'), default=True)
    is_staff = models.BooleanField(_('?????? ????????? ??????'), default=False)
    is_admin = models.BooleanField(_('??? ????????? ??????'), default=False)
    reg_date = models.DateTimeField(_('?????????'), auto_now_add=True)

    USERNAME_FIELD = 'user_id'
    REQUIRED_FIELDS = ['name', 'email', 'call_sign']

    objects = UserManager()

    def save(self, *args, **kwargs):
        super(CustomUser, self).save(*args, **kwargs)

    @staticmethod
    def has_perm(perm, obj=None):
        # "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    @staticmethod
    def has_module_perms(app_label):
        # "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    class Meta:
        ordering = ['reg_date', ]
        db_table = 'custom_user'
        verbose_name = '??????'
        verbose_name_plural = '?????????'
