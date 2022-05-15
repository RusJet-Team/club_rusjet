from django.core.exceptions import ValidationError
from django.db import models


class CarouselItem(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Название слайда",
        unique=True,
    )
    title = models.CharField(
        max_length=150,
        verbose_name="Заголовок слайда",
    )
    text = models.TextField(
        verbose_name="Текст слайда",
    )
    button_text = models.CharField(
        max_length=20,
        verbose_name="Текст кнопки",
    )
    button_url = models.URLField(
        max_length=250,
        blank=True,
        verbose_name="Ссылка по кнопке",
    )
    image = models.ImageField(
        upload_to="images/main_page",
        verbose_name="Картинка слайда",
        help_text="Изображения только в формате jpg",
    )

    class Meta:
        verbose_name = "Слайд на главной странице"
        verbose_name_plural = "Слайды на главной странице"

    def __str__(self):
        return self.name

    def clean(self):
        if CarouselItem.objects.count() > 10:
            raise ValidationError("Можно завести только 10 слайдов. Проверьте количество.")
        return super().clean()


class Partner(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Название партнёра",
        unique=True,
    )
    image = models.ImageField(
        upload_to="images/partners",
        verbose_name="Логотип партнёра",
    )

    class Meta:
        verbose_name = "Партнёр внизу страницы"
        verbose_name_plural = "Партнёры внизу страницы"

    def __str__(self):
        return self.name

    def clean(self):
        if Partner.objects.count() > 10:
            raise ValidationError("Можно указать только 10 партнёров.")
        return super().clean()
