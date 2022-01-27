from django.db import models


class MainImage(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Название изображения",
        unique=True,
    )
    image = models.ImageField(
        upload_to="images/main_page",
        verbose_name="Фотография",
    )

    class Meta:
        verbose_name = "Изображение на странице заставки"
        verbose_name_plural = "Изображения на странице заставки"

    def __str__(self):
        return self.name
