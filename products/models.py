from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.

class Product(models.Model):
    feature_choices = (
        ('teen', 'teenagers'),
        ('adlt', 'adults'),
        ('boy', 'boys'),
        ('girl', 'girls'),
        ('man', 'mans'),
        ('wom', 'women'),
        ('sprt', 'sport'),
        ('csl', 'casual'),
        ('clth', 'clothes'),
        ('bg', 'bag'),
        ('shoe', 'shoe'),
        ('acsr', 'accessory'),
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()
    brand = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    picture_1 = models.ImageField(upload_to='products/')
    picture_2 = models.ImageField(upload_to='products/', blank=True)
    picture_3 = models.ImageField(upload_to='products/', blank=True)
    picture_4 = models.ImageField(upload_to='products/', blank=True)
    picture_5 = models.ImageField(upload_to='products/', blank=True)
    is_featured = models.BooleanField(default=True)
    features = MultiSelectField(choices=feature_choices)
    
