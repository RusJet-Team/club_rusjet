from ckeditor.fields import RichTextField
from django.db import models

from config.utils.slugify import slugify


class ProjectCategory(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Название категории",
    )
    slug = models.SlugField(
        max_length=70,
        blank=True,
        verbose_name="URL категории",
        help_text="Если оставить пустым, заполнится транслитом название категории",
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Категория проектов"
        verbose_name_plural = "Категории проектов"

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name="Название проекта",
    )
    title = models.CharField(
        max_length=500,
        verbose_name="Краткое описание",
    )
    text = RichTextField(
        verbose_name="Основной текст",
    )
    category = models.ForeignKey(
        ProjectCategory,
        on_delete=models.CASCADE,
        verbose_name="Категории",
    )
    images = models.ManyToManyField(
        "ProjectImage",
        related_name="project_images",
        verbose_name="Изображения",
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = [
            "name",
        ]
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"
        constraints = [
            models.UniqueConstraint(
                fields=["name", "title"],
                name="unique_name_for_title",
            ),
        ]


class ProjectImage(models.Model):
    image = models.ImageField(
        upload_to="images/projects/detail/",
        verbose_name="Изображение",
    )

    class Meta:
        verbose_name = "Изображение проекта"
        verbose_name_plural = "Изображения проекта"

    def __str__(self):
        return self.image.name
