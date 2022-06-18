from ckeditor.fields import RichTextField
from django.db import models

from config.utils.slugify import slugify


class EquipmentCategory(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Название категории",
    )
    category_slug = models.SlugField(
        max_length=70,
        blank=True,
        verbose_name="URL категории",
        help_text="Если оставить пустым, заполнится транслитом название категории",
    )
    image = models.ImageField(
        upload_to="images/equipment-category",
        verbose_name="Изображение категории",
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Категория оборудования"
        verbose_name_plural = "Категории оборудования"

    def __str__(self):
        return self.name


class EquipmentSubCategory(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Название категории",
    )
    subcategory_slug = models.SlugField(
        max_length=70,
        blank=True,
        verbose_name="URL категории",
        help_text="Если оставить пустым, заполнится транслитом название категории",
    )
    category = models.ForeignKey(
        EquipmentCategory,
        on_delete=models.CASCADE,
        related_name="categories",
        verbose_name="Категория",
    )
    image = models.ImageField(
        upload_to="images/equipment-category/subcategory",
        verbose_name="Изображение подкатегории",
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ["name"]
        verbose_name = "Подкатегория оборудования"
        verbose_name_plural = "Подкатегории оборудования"
        constraints = [
            models.UniqueConstraint(
                fields=["name", "category"],
                name="unique_subcategory_for_category",
            ),
        ]

    def __str__(self):
        return self.name


class EquipmentBrend(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Название бренда",
    )
    brend_slug = models.SlugField(
        max_length=70,
        blank=True,
        verbose_name="URL бренда",
        help_text="Если оставить пустым, заполнится транслитом название категории",
    )
    subcategory = models.ForeignKey(
        EquipmentSubCategory,
        on_delete=models.CASCADE,
        related_name="subcategories",
        verbose_name="Подкатегория",
    )
    image = models.ImageField(
        upload_to="images/equipment-category/brend",
        verbose_name="Изображение бренда",
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Бренд оборудования"
        verbose_name_plural = "Бренды оборудования"

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("equipment-brends", kwargs={"sub_slug": self.subcategory__sub_slug})


class EquipmentItemImage(models.Model):
    image = models.ImageField(
        upload_to="images/equipment-category/items/images",
        verbose_name="Изображения в карусели единицы оборудования",
    )
    equipment = models.ForeignKey(
        "EquipmentItem",
        on_delete=models.CASCADE,
        verbose_name="Оборудование",
    )

    class Meta:
        verbose_name = "Изображение единицы оборудования"
        verbose_name_plural = "Изображения единицы оборудования"

    def __str__(self):
        image_name = (self.image.name).split("/")[-1]
        return image_name


class EquipmentItemDocument(models.Model):
    document = models.FileField(
        upload_to="images/equipment-category/items/documents",
        verbose_name="Документ во вложении",
    )
    equipment = models.ForeignKey(
        "EquipmentItem",
        on_delete=models.CASCADE,
        verbose_name="Оборудование",
    )

    class Meta:
        verbose_name = "Документ единицы оборудования"
        verbose_name_plural = "Документы единицы оборудования"

    def __str__(self):
        document_name = (self.document.name).split("/")[-1]
        return document_name

    def name(self):
        return (self.document.name).split("/")[-1]


class EquipmentItemYoutubeVideoUrl(models.Model):
    video_url = models.CharField(
        max_length=150,
        verbose_name="Ссылка на видео YouTube",
    )
    equipment = models.ForeignKey(
        "EquipmentItem",
        on_delete=models.CASCADE,
        verbose_name="Оборудование",
    )

    class Meta:
        verbose_name = "Ссылка на видео YouTube"
        verbose_name_plural = "Ссылки на видео YouTube"

    def __str__(self):
        self.video_url


class EquipmentItem(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name="Название оборудования",
    )
    title = models.CharField(
        max_length=500,
        verbose_name="Краткое описание",
    )
    tech_data = RichTextField(
        verbose_name="Технические характеристики",
    )
    subcategory = models.ForeignKey(
        EquipmentSubCategory,
        on_delete=models.CASCADE,
        verbose_name="Подкатегория",
    )
    brend = models.ForeignKey(
        EquipmentBrend,
        on_delete=models.CASCADE,
        verbose_name="Бренд",
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = [
            "name",
        ]
        verbose_name = "Оборудование"
        verbose_name_plural = "Оборудование"
        constraints = [
            models.UniqueConstraint(
                fields=["name", "title"],
                name="unique_name_for_title_equipment",
            ),
        ]
