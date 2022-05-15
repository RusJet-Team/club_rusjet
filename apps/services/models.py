from django.db import models


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
        help_text="Изображения только в формате png 120*120",
    )
    slug = models.SlugField(unique=True, null=True, verbose_name="Адрес услуги в url сайта")
    text = models.TextField(
        blank=True,
        verbose_name="Подробное описание",
    )
    carousel_images = models.ManyToManyField(
        "ServiceCarouselImage",
        verbose_name="Изображения в карусели",
    )

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"

    def __str__(self):
        return self.name


class ServiceCarouselImage(models.Model):
    image = models.ImageField(
        upload_to="images/services/detail/",
        verbose_name="Изображения в карусели услуги",
    )

    class Meta:
        verbose_name = "Изображение услуги"
        verbose_name_plural = "Изображения услуги"

    def __str__(self):
        return self.image.name
