from django.db import models
from django.contrib.auth.models import User

# Модель токенов
class Token(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='token')
    amount = models.IntegerField(default=0)

    def add_tokens(self, amount):
        """Добавить токены пользователю."""
        self.amount += amount
        self.save()

    def subtract_tokens(self, amount):
        """
        Списать токены у пользователя.
        Возвращает True, если достаточно токенов, иначе False.
        """
        if self.amount >= amount:
            self.amount -= amount
            self.save()
            return True
        return False

    def __str__(self):
        return f"{self.user.username} — {self.amount} токенов"

# Модель профиля
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    avatar_url = models.URLField(
        blank=True,
        null=True,
        default='https://img5tv.cdnvideo.ru/shared/files/202212/1_1632199.png'
    )

    def __str__(self):
        return f"Профиль {self.user.username}"
