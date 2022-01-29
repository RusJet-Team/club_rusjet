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

    # def save(self, *args, **kwargs):
    #     print(self.id)
    #     print(dir(self.image))
    #     print(self.image.name)
    #     self.image.name = "333.jpg"
    #     # print(self.image.storage.generate_filename(filename="12"))
    #     # print(self.image.storage.get_available_name(name="qwert"))
    #     # print(dir(self.image.storage))
    #     super(MainImage, self).save(*args, **kwargs)

    # def delete(self, *args, **kwargs):
    #     storage, path = self.image.storage, self.image.path
    #     super(MainImage, self).delete(*args, **kwargs)
    #     storage.delete(path)
