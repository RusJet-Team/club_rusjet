from django.db import models


class Service(models.Model):
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

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"

    def __str__(self):
        return self.name
