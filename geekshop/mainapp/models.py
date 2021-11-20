from django.db import models

# Create your models here.
class ProductCategory(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

class Product(models.Model):
    name = models.CharField(max_length=128)
    image = models.ImageField(upload_to='product_image', blank=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} | {self.category}'

# >>> from mainapp.models import ProductCategory
# >>> category = ProductCategory(name= 'Одежда', description = 'Описание одежды')
# >>> category.save()
# >>> category_1 = ProductCategory.objects.create(name='Аксессуары', description ='')
# >>> category_2 = ProductCategory.objects.create(name='Обувь', description ='')
# >>> a = ProductCategory.objects.get(name='Одежда')
# >>> print(a)
# Одежда
# >>> print(a.description)
# Описание одежды
# >>> a = ProductCategory.objects.all()
# >>> for i in a:
# ...     print(i)
# ...
# Одежда
# Аксессуары
# Обувь
# >>>

