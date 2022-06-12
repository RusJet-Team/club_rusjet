from ckeditor.fields import RichTextField
from django.db import models


class ClubMember(models.Model):
    first_name = models.CharField(
        max_length=50,
        verbose_name="Имя",
    )
    last_name = models.CharField(
        max_length=50,
        verbose_name="Фамилия",
    )
    middle_name = models.CharField(
        max_length=50,
        verbose_name="Отчество",
    )
    vocation = models.CharField(
        max_length=50,
        verbose_name="Должность",
    )
    image = models.ImageField(
        upload_to="images/club/members/",
        verbose_name="Фотография",
        help_text="Изображения только в формате jpg",
    )
    email = models.EmailField(
        max_length=150,
        blank=True,
        unique=True,
        verbose_name="Электронная почта",
        help_text="Необязательно",
    )

    class Meta:
        verbose_name = "Член клуба"
        verbose_name_plural = "Члены клуба"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class HalfStaticPage(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Название страницы",
    )
    slug = models.SlugField(
        unique=True,
        verbose_name="URL страницы",
    )
    text = RichTextField(
        verbose_name="Текст",
    )

    class Meta:
        verbose_name = "Статическая страница"
        verbose_name_plural = "Статические страницы"

    def __str__(self):
        return self.name


class HalfStaticPageImage(models.Model):
    image = models.ImageField(
        upload_to="images/club/staticpages/",
        verbose_name="Изображения для вставки на страницу",
    )
    page = models.ForeignKey(
        HalfStaticPage,
        on_delete=models.CASCADE,
        verbose_name="Статическая страница",
    )

    class Meta:
        verbose_name = "Изображение статических страниц"
        verbose_name_plural = "Изображения статических страниц"

    def __str__(self):
        image_name = (self.image.name).split("/")[-1]
        return image_name
