from ckeditor.fields import RichTextField
from django.core.exceptions import ValidationError
from django.db import models

from config.utils.slugify import slugify


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
    my_order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
        verbose_name="Порядок отображения",
    )

    class Meta:
        verbose_name = "Слайд на главной странице"
        verbose_name_plural = "Слайды на главной странице"
        ordering = ["my_order"]

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
    short_description = models.CharField(
        max_length=250,
        verbose_name="Краткое описание",
        blank=True,
    )
    image = models.ImageField(
        upload_to="images/partners",
        verbose_name="Логотип партнёра",
    )
    text = RichTextField(
        verbose_name="Подробное описание",
        blank=True,
    )
    url = models.URLField(
        max_length=200,
        blank=True,
        verbose_name="Ссылка на страницу с оборудованием",
        help_text="Если оставить пустым, нельзя будет указать ссылку на страницу с оборудованием",
    )
    slug = models.SlugField(
        unique=True,
        null=True,
        verbose_name="Url партнёра на сайте",
        help_text="Если оставить пустым, заполнится транслитом название партнёра",
    )
    my_order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
        verbose_name="Порядок отображения",
    )

    class Meta:
        verbose_name = "Партнёр"
        verbose_name_plural = "Партнёры"
        ordering = ["my_order"]

    def __str__(self):
        return self.name

    def clean(self):
        if Partner.objects.count() > 10:
            raise ValidationError("Можно указать только 10 партнёров.")
        return super().clean()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
