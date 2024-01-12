from django.db import models
from django.contrib.auth.models import AbstractUser

class AllProducts(models.Model):
    uniq_id = models.CharField(max_length=50, unique=True)
    crawl_timestamp = models.DateTimeField()
    product_url = models.URLField()
    product_name = models.CharField(max_length=255)
    product_category_tree = models.TextField()
    pid = models.CharField(max_length=50)
    retail_price = models.DecimalField(max_digits=10, decimal_places=2)
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.TextField()
    is_FK_Advantage_product = models.BooleanField()
    description = models.TextField()
    product_rating = models.CharField(max_length=50)
    overall_rating = models.CharField(max_length=50)
    brand = models.CharField(max_length=255)
    product_specifications = models.TextField()

    def __str__(self):
        return self.product_name


class CustomUser(AbstractUser):
    pass




class RelaxedFit(models.Model):
    product = models.OneToOneField(AllProducts, on_delete=models.CASCADE)
    fabric = models.CharField(max_length=255, blank=True, null=True)
    idealfor = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"RelaxedFit for {self.product.product_name}"


class RegularFit(models.Model):
    product = models.OneToOneField(AllProducts, on_delete=models.CASCADE)
    fabric = models.CharField(max_length=255, blank=True, null=True)
    idealfor = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"RegularFit for {self.product.product_name}"