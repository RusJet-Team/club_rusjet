from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models

from config.utils.slugify import slugify


class NewsCategory(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Название категории",
    )
    slug = models.SlugField(
        max_length=70,
        blank=True,
        verbose_name="URL категории",
        help_text="Если оставить пустым, заполнится транслитом название категории",
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Категория новости"
        verbose_name_plural = "Категории новостей"

    def __str__(self):
        return self.name


class News(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name="Название новости",
    )
    title = models.CharField(
        max_length=500,
        verbose_name="Краткое описание",
    )
    text = RichTextField(
        verbose_name="Основной текст",
    )
    pub_date = models.DateField(
        auto_now_add=True,
        verbose_name="Дата публикации",
    )
    image = models.ImageField(
        blank=True,
        upload_to="images/news",
        verbose_name="Фотография для новости",
    )
    pub_user = models.ForeignKey(
        User,
        on_delete=models.RESTRICT,
        editable=False,
        null=True,
        blank=True,
        verbose_name="Автор новости",
    )
    category = models.ManyToManyField(
        NewsCategory,
        related_name="news",
        verbose_name="Категории",
    )
    geolocation_url = models.TextField(
        verbose_name="Геолокация",
        blank=True,
        help_text="Если нужна геолокация,необходимо вставить кусок html кода с https://yandex.ru/maps",
    )
    event_bool = models.BooleanField(
        default=False,
        verbose_name="Мероприятие",
    )
    event_date = models.DateField(
        null=True,
        blank=True,
        verbose_name="Дата мероприятия",
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = [
            "-pub_date",
        ]
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        constraints = [
            models.UniqueConstraint(
                fields=["name", "pub_date", "title"],
                name="unique_name_for_pub_date",
            ),
        ]
