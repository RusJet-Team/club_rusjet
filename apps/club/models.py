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

    class Meta:
        verbose_name = "Член клуба"
        verbose_name_plural = "Члены клуба"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
