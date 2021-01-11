from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator, MinValueValidator
from django.db import models
from django.urls import reverse


def validate_image(fieldfile_obj):
    filesize = fieldfile_obj.file.size
    megabyte_limit = 2000000
    if filesize > megabyte_limit:
        raise ValidationError("Размер файла не может быть больше 2Мб" % str(megabyte_limit))


class IndexPage(models.Model):
    page_title = models.CharField("Заголовок страницы", max_length=256)
    keywords = models.TextField("Ключевые слова", blank=True, null=True)
    description = models.TextField("Описание", blank=True, null=True)
    headline = models.CharField("Заголовок текста главной страницы", max_length=256, blank=True, null=True)
    latitude = models.DecimalField("Широта", max_digits=4, decimal_places=2, blank=True, null=True,
                                   validators=[MinValueValidator(0)])
    longitude = models.DecimalField("Долгота", max_digits=4, decimal_places=2, blank=True, null=True,
                                    validators=[MinValueValidator(0)])
    photo_width = models.PositiveIntegerField("Ширина фото слайдера", default=1240, null=True, blank=True)
    photo_height = models.PositiveIntegerField("Высота фото слайдера", default=833, null=True, blank=True)

    class Meta:
        verbose_name = "Главная страница сайта"
        verbose_name_plural = "Редактирование главной страницы"

    def __str__(self):
        return "Редактировать"


class Photo(models.Model):
    headline = models.ForeignKey(IndexPage, verbose_name="Главная страница", on_delete=models.CASCADE)
    image = models.ImageField("Фотография слайдера главной страницы", upload_to='sliders/',
                              validators=[validate_image, FileExtensionValidator(['jpg', 'jpeg'])])
    name = models.CharField("Название фотографии", max_length=256)

    class Meta:
        verbose_name = "Фотография"
        verbose_name_plural = "Фотографии"


class Paragraph(models.Model):
    text = models.TextField("Текст")
    headline = models.ForeignKey(IndexPage, verbose_name="Главная страница", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Абзац"
        verbose_name_plural = "Абзацы"


class Product(models.Model):
    page_title = models.CharField("Заголовок страницы", max_length=256)
    keywords = models.TextField("Ключевые слова", blank=True, null=True)
    description = models.TextField("Описание", blank=True, null=True)
    name = models.CharField("Название продукта", max_length=256, blank=True, null=True)
    created = models.DateTimeField("Дата и время добавления", auto_now_add=True)
    photo = models.ImageField("Фотография продукта", upload_to='products/', blank=True, null=True,
                              validators=[validate_image, FileExtensionValidator(['jpg', 'jpeg'])])
    photo_width = models.PositiveIntegerField("Ширина фотографии", default=1240, null=True, blank=True)
    photo_height = models.PositiveIntegerField("Высота фотографии", default=992, null=True, blank=True)
    url = models.SlugField("Ссылка", max_length=130, unique=True)

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Редактирование продуктов"

    def __str__(self):
        return self.url

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"slug": self.url})


class Option(models.Model):
    title = models.CharField("Заголовок списка опций", max_length=256)
    product = models.ForeignKey(Product, verbose_name="Продукт", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Заголовок списка опций"
        verbose_name_plural = "Заголовки списков опций"

    def __str__(self):
        return ''


class Suboption(models.Model):
    text = models.TextField("Пункт списка")
    option = models.ForeignKey(Option, verbose_name="Опции", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Пункт списка"
        verbose_name_plural = "Пункты списка"

    def __str__(self):
        return ''
