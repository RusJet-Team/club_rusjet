from django.db import models


class Question(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Имя человека",
    )
    email = models.EmailField(
        max_length=150,
        verbose_name="Email для контактов",
    )
    text = models.TextField(
        verbose_name="Текст запроса или вопроса",
    )

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"

    def __str__(self):
        return self.name
