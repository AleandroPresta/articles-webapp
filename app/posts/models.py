from django.db import models
from django.contrib.auth.models import User

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

# Create your models here.
class Post(models.Model):
    # Define the available categories

    title = models.CharField(max_length=50)
    body = models.TextField()
    slug = models.SlugField()
    category = models.CharField(default='OTR', max_length=4, choices=CATEGORY_CHOICES)
    date = models.DateTimeField(auto_now_add=True)
    banner = models.ImageField(default='../static/assets/fallback.webp', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    
    class Meta:
        ordering = ['-date']
    
    def __str__(self) -> str:
        return self.title
    
    @staticmethod
    def convert_name_to_code(name):
        for code, category in CATEGORY_CHOICES:
            if category == name:
                return code
        return 'OTR'
    
    def convert_code_to_name(code):
        for category, name in CATEGORY_CHOICES:
            if category == code:
                return name
        return 'Other'
    

class Comment(models.Model):
    body = models.TextField(default='')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.body