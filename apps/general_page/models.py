# from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.general_page.constants import MAIN_IMAGE_NAMES


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

    def save(self, *args, **kwargs):
        try:
            this = MainImage.objects.get(id=self.id)
            storage, path = this.image.storage, this.image.path
            storage.delete(path)
            if self.id in MAIN_IMAGE_NAMES.keys():
                self.image.name = MAIN_IMAGE_NAMES[self.id]
        except MainImage.DoesNotExist as error:
            raise (error)
        super(MainImage, self).save(*args, **kwargs)


class SocialNetwork(models.Model):
    class SocialNetworkType(models.TextChoices):
        YOUTUBE = "youtube", _("YouTube")
        INSTAGRAM = "instagram", _("Instagram")
        FACEBOOK = "facebook", _("FaceBook")
        VKONTAKTE = "vk", _("VKontakte")

    type = models.CharField(
        max_length=9,
        choices=SocialNetworkType.choices,
        verbose_name="Тип социальной сети",
    )
    url = models.URLField(
        max_length=200,
        verbose_name="Ссылка на социальную сеть",
    )
    is_visible = models.BooleanField(
        default=False,
        verbose_name="Отображение на главной странице",
        help_text=("Показывать это соц. сеть на главной?"),
    )

    class Meta:
        verbose_name = "Социальная сеть"
        verbose_name_plural = "Социальные сети"
        ordering = ("type",)

    def __str__(self):
        return self.type

    # def clean(self):
    #     if SocialNetwork.objects.filter(type=self.type).exists():
    #         raise ValidationError(f"{self.type} - уже добавлена! Редактируйте существующую.")


# class InscriptionOnManePage(models.Model):
#     settings_key = models.SlugField(
#         max_length=40,
#         verbose_name="Ключ настройки",
#         unique=True,
#     )
#     name = models.CharField(
#         max_length=50,
#         verbose_name="Название надписи",
#     )
#     value = models.CharField(
#         max_length=250,
#         verbose_name="Надпись",
#     )

#     class Meta:
#         ordering = ("name",)
#         verbose_name = "Надпись на главной"
#         verbose_name_plural = "Надписи на главной"

#     def __str__(self):
#         return self.settings_key

#     @classmethod
#     def get_setting(cls, settings_key):
#         if InscriptionOnManePage.objects.filter(settings_key=settings_key).exists():
#             setting = InscriptionOnManePage.objects.get(settings_key=settings_key)
#             return setting.value
