from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, first_name, last_name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('User must have an email adress')
        email = self.normalize_email(email=email)
        user = self.model(email=email, first_name=first_name,
                          last_name=last_name)

        user.setpassword(password=password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, first_name, last_name, password=None):
        """Create and save a new superuser with given details"""
        user = self.create_user(
            email=email, first_name=first_name, last_name=last_name)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def get_full_name(self):
        """Retrieve full name of user"""
        return f"{self.first_name} {self.last_name}"

    def get_short_name(self):
        """Retrieve short name of user"""
        return self.first_name

    def __str__(self) -> str:
        """Return string representation of our user"""
        return self.email
