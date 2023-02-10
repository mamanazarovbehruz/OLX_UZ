from django.db import models
from random import sample
from django.core.validators import MinValueValidator

from api.v1.accounts.models import CustomUser
from api.v1.accounts.services import upload_product_path
from api.v1.accounts.validators import validate_phone
from .enums import ValueType, Status


class Category(models.Model):
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=200, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_delete = models.BooleanField(default=False)

    creator = models.ForeignKey(
        CustomUser, related_name='categories',
        on_delete=models.SET_NULL, null=True)

    def save(self, *args, **kwargs):
        self.name = ' '.join(self.name.strip().split())
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Field(models.Model):
    categories = models.ManyToManyField(Category)
    creator = models.ForeignKey(CustomUser, related_name='category_fields', null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=150, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    is_delete = models.BooleanField(default=False)


    def save(self, *args, **kwargs):
        self.name = ' '.join(self.name.strip().split())
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Product(models.Model):
    # CharField
    number_id = models.CharField(max_length=8, unique=True)
    title = models.CharField(max_length=250)
    value_type = models.CharField(max_length=1, choices=ValueType.choices())
    region = models.CharField(max_length=50)
    district = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=13, validators=[validate_phone])
    status = models.CharField(max_length=2, choices=Status.choices(), default=Status.n.name)

    # BoolenField
    is_agreement = models.BooleanField(default=False)
    price_is_dollar = models.BooleanField(default=False)
    is_new = models.BooleanField(default=False)
    is_business = models.BooleanField(default=False)
    is_auto_renewal = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)

    # TextField
    description = models.TextField(max_length=9000, blank=True)

    price = models.FloatField(default=0, validators=[MinValueValidator(0.0)])
    views = models.PositiveSmallIntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    # Image
    main_image = models.ImageField(upload_to=upload_product_path, blank=True)
    image1 = models.ImageField(upload_to=upload_product_path, blank=True)
    image2 = models.ImageField(upload_to=upload_product_path, blank=True)
    image3 = models.ImageField(upload_to=upload_product_path, blank=True)
    image4 = models.ImageField(upload_to=upload_product_path, blank=True)
    image5 = models.ImageField(upload_to=upload_product_path, blank=True)


    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    author = models.ForeignKey(CustomUser, related_name='products', on_delete=models.SET_NULL, null=True)

    def save(self, *args, **kwargs):
        self.number_id = sample(range(100), 8)
        if Product.objects.filter(number_id=self.number_id).exists():
            self.number_id = sample(range(10), 8)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class ProductField(models.Model):
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    author = models.ForeignKey(
        CustomUser, related_name='productfields',
        on_delete=models.SET_NULL, null=True
    )
    is_deleted = models.BooleanField(default=False)

    # first choice
    text = models.CharField(max_length=255, blank=True)

    # second Choice
    is_true = models.BooleanField(default=False)

    date_created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.text = ' '.join(self.text.strip().split())
        super().save(*args, **kwargs)

    def __str__(self):
        return self.field