from django.db import models
from django.contrib.auth.models import User
# Create your models here.
CATEGORY_CHOICE=(
    ('CR','Crud'),
    ('MK','Milk'),
    ('LS','Lassi'),
    ('MS','MilkShake'),
    ('PN','Paneer'),
    ('GH','Ghee'),
    ('CZ','Cheese'),
    ('IH','Ice-cream'),
)

class Products(models.Model):
    title=models.CharField(max_length=150)
    selling_price=models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    composition = models.TextField(default='')
    prodapp= models.TextField(default='')
    category = models.CharField(choices=CATEGORY_CHOICE,max_length=2)
    product_image = models.ImageField(upload_to='product')
    product_quantity = models.FloatField()
    def __str__(self):
        return self.title

STATE_CHOICE=(
    ('KERALA','KERALA'),
    ('TAMILNADU','TAMILNADU'),
    ('KARNATAK','KARNATAK'),
    ('ANDRAPREDEH','ANDRAPREDEH'),
    ('GUJARATH','GUJARATH'),
    ('RAJASTHA','RAJASTHA'),
    ('MAHARASTRA','MAHARASTRA'),
    ('MADHYAPRESHES','MADHYAPRESHES'),
    ('UP','UP'),
    ('BENGOL','BENGOL'),
    ('GOA','GOA'),
    ('ARUNACHAL','ARUNACHA'),
    ('ORISA','ORISA'),
    ('CHARGAND','CHARGAND'),
    ('SIKIM','SIKIM'),
    ('MEGALAYA','MEGALAYA'),
    ('JAMMU','JAMMU'),
    ('ORISA','ORISA'),
    ('HARIYANA','HARIYANA'),
    ('HIMACHA','HIMACHAL'),
    ('ASSAM','ASSAM'),
    ('CHANDIGAND','CHANDIGAND'),
)
class customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    mobile = models.IntegerField(default=0)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICE,max_length=100)
    def __str__(self):
        return self.name

