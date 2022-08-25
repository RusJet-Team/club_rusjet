from ckeditor.fields import RichTextField
from django.db import models

from config.utils.slugify import slugify


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

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"

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

    class Meta:
        verbose_name = "Изображение услуги"
        verbose_name_plural = "Изображения услуги"

    def __str__(self):
        image_name = (self.image.name).split("/")[-1]
        return image_name
