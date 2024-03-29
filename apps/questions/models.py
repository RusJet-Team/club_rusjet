from django.core.validators import MinLengthValidator
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Question(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Ваше имя",
    )
    email = models.EmailField(
        max_length=150,
        verbose_name="Email",
    )
    phone_number = PhoneNumberField(
        verbose_name="Телефон",
        blank=True,
    )
    text = models.TextField(
        verbose_name="Ваш вопрос",
        validators=[MinLengthValidator(10)],
    )

    class Meta:
        verbose_name = "Общий вопрос"
        verbose_name_plural = "Общие вопросы"

    def __str__(self):
        return self.name
