from ckeditor.fields import RichTextField
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# from config.utils.image_change import crop_square_and_resize
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
        help_text="Для лучшего отображения должно быть равное соотношение сторон",
    )

    def save(self, *args, **kwargs):
        if not self.category_slug:
            self.category_slug = slugify(self.name)
        super().save(*args, **kwargs)
        # img = crop_square_and_resize(self.image.path)
        # img.save(self.image.path)

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
        help_text="Для лучшего отображения должно быть равное соотношение сторон",
    )

    def save(self, *args, **kwargs):
        if not self.subcategory_slug:
            self.subcategory_slug = slugify(self.name)
        super().save(*args, **kwargs)
        # img = crop_square_and_resize(self.image.path)
        # img.save(self.image.path)

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
        help_text="Для лучшего отображения должно быть равное соотношение сторон",
    )

    def save(self, *args, **kwargs):
        if not self.brend_slug:
            self.brend_slug = slugify(self.name)
        super().save(*args, **kwargs)
        # img = crop_square_and_resize(self.image.path)
        # img.save(self.image.path)

    class Meta:
        verbose_name = "Бренд оборудования"
        verbose_name_plural = "Бренды оборудования"

    def __str__(self):
        return self.name


class EquipmentItemImage(models.Model):
    image = models.ImageField(
        upload_to="images/equipment-category/items/images",
        verbose_name="Изображения в карусели единицы оборудования",
        help_text="Для лучшего отображения должно быть равное соотношение сторон",
    )
    equipment = models.ForeignKey(
        "EquipmentItem",
        on_delete=models.CASCADE,
        verbose_name="Оборудование",
    )
    my_order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
        verbose_name="Порядок отображения",
    )

    class Meta:
        verbose_name = "Изображение единицы оборудования"
        verbose_name_plural = "Изображения единицы оборудования"
        ordering = ["my_order"]

    def __str__(self):
        image_name = (self.image.name).split("/")[-1]
        return image_name

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     img = crop_square_and_resize(self.image.path)
    #     img.save(self.image.path)

    def clean(self):
        height = 400
        width = 400
        if self.image.height < height or self.image.width < width:
            raise ValidationError(f"Размеры изображения должны быть не менее {height}x{width}")


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
    my_order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
        verbose_name="Порядок отображения",
    )

    class Meta:
        verbose_name = "Документ единицы оборудования"
        verbose_name_plural = "Документы единицы оборудования"
        ordering = ["my_order"]

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
    my_order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
        verbose_name="Порядок отображения",
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["my_order"]
        verbose_name = "Оборудование"
        verbose_name_plural = "Оборудование"
        constraints = [
            models.UniqueConstraint(
                fields=["name", "title"],
                name="unique_name_for_title_equipment",
            ),
        ]


class LastViewedEquipmentItem(models.Model):
    session = models.CharField(
        max_length=200,
        verbose_name="Ключ сессии",
    )
    equipment_item = models.ForeignKey(
        EquipmentItem,
        on_delete=models.CASCADE,
        verbose_name="Оборудование",
    )


class EquipmentRequest(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Ваше имя",
        help_text="Пожалуйста, представьтесь",
    )
    email = models.EmailField(
        max_length=150,
        verbose_name="Email",
        help_text="Укажите, чтобы связаться с Вами",
    )
    phone_number = PhoneNumberField(verbose_name="Телефон", blank=True, help_text="Необязательно")
    text = models.TextField(
        verbose_name="Ваш запрос",
        validators=[MinLengthValidator(10)],
        help_text="Укажите количество, так же можно указать необходимую периферию и комплектующие",
    )

    class Meta:
        verbose_name = "Запрос"
        verbose_name_plural = "Запросы оборудования"

    def __str__(self):
        return self.name
