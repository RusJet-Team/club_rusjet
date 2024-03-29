from ckeditor.fields import RichTextField
from django.db import models

from config.utils.youtube_links import get_current_link


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
    achievements = models.TextField(
        verbose_name="Достижения",
    )
    image = models.ImageField(
        upload_to="images/club/members/",
        verbose_name="Фотография",
        help_text="Изображения только в формате jpg",
    )
    my_order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
        verbose_name="Порядок отображения",
    )

    class Meta:
        verbose_name = "Член клуба"
        verbose_name_plural = "Члены клуба"
        ordering = ["my_order"]

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
        verbose_name="Изображения для вставки в карусель",
    )
    page = models.ForeignKey(
        HalfStaticPage,
        on_delete=models.CASCADE,
        verbose_name="Статическая страница",
    )
    my_order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
        verbose_name="Порядок отображения",
    )

    class Meta:
        verbose_name = "Изображение карусели статических страниц"
        verbose_name_plural = "Изображения карусели статических страниц"
        ordering = ["my_order"]

    def __str__(self):
        image_name = (self.image.name).split("/")[-1]
        return image_name


class HalfStaticPageYoutubeVideoUrl(models.Model):
    video_url = models.CharField(
        max_length=150,
        verbose_name="Ссылка на видео YouTube",
    )
    equipment = models.ForeignKey(
        HalfStaticPage,
        on_delete=models.CASCADE,
        verbose_name="Статическая страница",
    )
    my_order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
        verbose_name="Порядок отображения",
    )

    class Meta:
        verbose_name = "Ссылка на видео YouTube"
        verbose_name_plural = "Ссылки на видео YouTube"
        ordering = ["my_order"]

    def __str__(self):
        self.video_url

    def save(self, *args, **kwargs):
        self.video_url = get_current_link(self.video_url)
        super().save(*args, **kwargs)
