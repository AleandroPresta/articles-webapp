from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    # Define the available categories
    CATEGORY_CHOICES = [
        ('NAT', 'Nature'),
        ('TECH', 'Technology'),
        ('LIFE', 'Lifestyle'),
        ('FIN', 'Finance'),
        ('EDU', 'Education'),
        ('ENT', 'Entertainment'),
        ('HEAL', 'Health'),
        ('FOOD', 'Food & Drink'),
        ('TRVL', 'Travel'),
        ('SPT', 'Sports'),
        ('BUS', 'Business'),
        ('SCI', 'Science'),
        ('POL', 'Politics'),
        ('ART', 'Art & Culture'),
        ('MUS', 'Music'),
        ('MOV', 'Movies & TV'),
        ('AUTO', 'Automotive'),
        ('DIY', 'DIY & Crafts'),
        ('FASH', 'Fashion'),
        ('GAM', 'Gaming'),
        ('PETS', 'Pets'),
        ('PHOT', 'Photography'),
        ('HOME', 'Home & Garden'),
        ('REL', 'Religion & Spirituality'),
        ('OTR', 'Other')
    ]

    title = models.CharField(max_length=50)
    body = models.TextField()
    slug = models.SlugField()
    category = models.CharField(default='OTR', max_length=4, choices=CATEGORY_CHOICES)
    date = models.DateTimeField(auto_now_add=True)
    banner = models.ImageField(default='../static/assets/fallback.webp', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    
    def __str__(self) -> str:
        return self.title