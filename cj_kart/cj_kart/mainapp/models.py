from django.db import models

# Create your models here.
CATEGORY_CHOICE=(
    ('CR','Crud'),
    ('ML','Milk'),
    ('LS','Lassi'),
    ('MS','MilkShake'),
    ('PN','Paneer'),
    ('GH','Ghee'),
    ('CZ','Cheese'),
    ('IC','Ice-cream'),
)


class Product(models.Model):
    title=models.CharField(max_length=150)
    selling_price=models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    composition = models.TextField(default='')
    prodapp= models.TextField(default='')
    category = models.CharField(choices=CATEGORY_CHOICE,max_length=2)
    product_image = models.ImageField(upload_to='product')
    def __str__(self):
        return self.title