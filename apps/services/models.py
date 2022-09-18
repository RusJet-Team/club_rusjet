from ckeditor.fields import RichTextField
from django.db import models

from config.utils.slugify import slugify
from config.utils.youtube_links import get_current_link


class ServiceItem(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Название услуги",
    )
    short_description = models.CharField(
        max_length=250,
        verbose_name="Краткое описание",
    )
    image = models.ImageField(
        upload_to="images/services/",
        verbose_name="Значок на главной странице",
        help_text="Изображения только в формате png 100*100",
    )
    slug = models.SlugField(
        unique=True,
        null=True,
        verbose_name="Url услуги на сайте",
        help_text="Если оставить пустым, заполнится транслитом название услуги",
    )
    text = RichTextField(
        verbose_name="Подробное описание",
    )
    my_order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
        verbose_name="Порядок отображения",
    )

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"
        ordering = ["my_order"]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class ServiceCarouselImage(models.Model):
    image = models.ImageField(
        upload_to="images/services/detail/",
        verbose_name="Изображения в карусели услуги",
    )
    service = models.ForeignKey(
        ServiceItem,
        on_delete=models.CASCADE,
        verbose_name="Услуга",
    )
    my_order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
        verbose_name="Порядок отображения",
    )

    class Meta:
        verbose_name = "Изображение услуги"
        verbose_name_plural = "Изображения услуги"
        ordering = ["my_order"]

    def __str__(self):
        image_name = (self.image.name).split("/")[-1]
        return image_name


class ServiceYoutubeVideoUrl(models.Model):
    video_url = models.CharField(
        max_length=150,
        verbose_name="Ссылка на видео YouTube",
    )
    service = models.ForeignKey(
        ServiceItem,
        on_delete=models.CASCADE,
        verbose_name="Услуга",
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
