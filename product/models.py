from django.db import models
from django.conf import settings


class Product(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    created_at = models.DateField(auto_now_add=True)
    modified_at = models.DateField(auto_now=True)
    likes_counter = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class Comment(models.Model):
    author = models.CharField(max_length=255)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey('Product')

    def __str__(self):
        return self.author + ' - ' + self.product.name

    class Meta:
        ordering = ['-created_at']


class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    product = models.ForeignKey('Product')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username + ' - ' + self.product.name




# Create your models here.
