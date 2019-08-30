from django.contrib.auth.models import BaseUserManager
from django.core.management.utils import get_random_secret_key


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, full_name, username, password, language, time_zone, **extra_fields):
        email = email.strip().lower()
        user = self.model(
            email=email,
            full_name=full_name,
            username=username,
            language=language,
            time_zone=time_zone,
            **extra_fields
        )
        user.jwt_secret_key = get_random_secret_key()
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, full_name, username, password, language, time_zone, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, full_name, username, password, language, time_zone, **extra_fields)

    def create_superuser(self, email, full_name, username, password,
                         language='pt-BR', time_zone='America/Sao_Paulo', **extra_fields):
        extra_fields.setdefault('is_premium', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, full_name, username, password, language, time_zone, **extra_fields)
