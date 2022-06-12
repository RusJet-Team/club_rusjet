# from ckeditor.fields import RichTextField
# from django.db import models

# from config.utils.slugify import slugify


# class EquipmentCategory(models.Model):
#     name = models.CharField(
#         max_length=50,
#         verbose_name="Название категории",
#     )
#     slug = models.SlugField(
#         max_length=70,
#         blank=True,
#         verbose_name="URL категории",
#         help_text="Если оставить пустым, заполнится транслитом название категории",
#     )
#     image = models.ImageField(
#         upload_to="images/equipment-category",
#         verbose_name="Изображение категории",
#     )

#     def save(self, *args, **kwargs):
#         if not self.slug:
#             self.slug = slugify(self.name)
#         super().save(*args, **kwargs)

#     class Meta:
#         verbose_name = "Категория оборудования"
#         verbose_name_plural = "Категории оборудования"

#     def __str__(self):
#         return self.name

# class EquipmentSubCategory(models.Model):
#     name = models.CharField(
#         max_length=50,
#         verbose_name="Название категории",
#     )
#     slug = models.SlugField(
#         max_length=70,
#         blank=True,
#         verbose_name="URL категории",
#         help_text="Если оставить пустым, заполнится транслитом название категории",
#     )
#     category = models.ForeignKey(
#         EquipmentCategory,
#         on_delete=models.CASCADE,
#         related_name="categories",
#         verbose_name="Категория",
#     )
#     image = models.ImageField(
#         upload_to="images/equipment-category/subcategory",
#         verbose_name="Изображение подкатегории",
#     )

#     def save(self, *args, **kwargs):
#         if not self.slug:
#             self.slug = slugify(self.name)
#         super().save(*args, **kwargs)

#     class Meta:
#         ordering = ["name"]
#         verbose_name = "Подкатегория оборудования"
#         verbose_name_plural = "Подкатегории оборудования"
#         constraints = [
#             models.UniqueConstraint(
#                 fields=["name", "category"],
#                 name="unique_subcategory_for_category",
#             ),
#         ]

#     def __str__(self):
#         return self.name

# class EquipmentBrend(models.Model):
#     name = models.CharField(
#         max_length=50,
#         verbose_name="Название бренда",
#     )
#     slug = models.SlugField(
#         max_length=70,
#         blank=True,
#         verbose_name="URL бренда",
#         help_text="Если оставить пустым, заполнится транслитом название категории",
#     )
#     subcategory = models.ForeignKey(
#         EquipmentSubCategory,
#         on_delete=models.CASCADE,
#         related_name="subcategories",
#         verbose_name="Подкатегория",
#     )
#     image = models.ImageField(
#         upload_to="images/equipment-category/brend",
#         verbose_name="Изображение бренда",
#     )

#     def save(self, *args, **kwargs):
#         if not self.slug:
#             self.slug = slugify(self.name)
#         super().save(*args, **kwargs)

#     class Meta:
#         verbose_name = "Бренд оборудования"
#         verbose_name_plural = "Бренды оборудования"

#     def __str__(self):
#         return self.name

# class EquipmentItemImage(models.Model):
#     image = models.ImageField(
#         upload_to="images/equipment-category/items/images",
#         verbose_name="Изображения в карусели еденицы оборудования",
#     )

#     class Meta:
#         verbose_name = "Изображение единицы оборудования"
#         verbose_name_plural = "Изображения единицы оборудования"

#     def __str__(self):
#         image_name = (self.image.name).split("/")[-1]
#         return image_name

# class EquipmentItemDocument(models.Model):
#     document = models.FileField(
#         upload_to="images/equipment-category/items/documents",
#         verbose_name="Изображения в карусели еденицы оборудования",
#     )

#     class Meta:
#         verbose_name = "Документ единицы оборудования"
#         verbose_name_plural = "Документы единицы оборудования"

#     def __str__(self):
#         document_name = (self.document.name).split("/")[-1]
#         return document_name

# class EquipmentItemYoutubeVideUrl(models.Model):
#     video_url = name = models.CharField(
#         max_length=150,
#         verbose_name="Ссылка на видео YouTube",
#     )

#     class Meta:
#         verbose_name = "Ссылка на"
#         verbose_name_plural = "Документы единицы оборудования"

#     def __str__(self):
#         document_name = (self.document.name).split("/")[-1]
#         return document_name

# class EquipmentItem(models.Model):
#     pass
