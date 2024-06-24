from django.db import models
from django.contrib.auth.models import User


class Hotel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Package(models.Model):
    name = models.CharField(max_length=100, unique=True)
    overview = models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    hotels = models.ManyToManyField(Hotel, related_name='packages', blank=True)

    def __str__(self):
        return self.name


class Image(models.Model):
    package = models.ForeignKey(Package, related_name='images_set', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='packages/image/')

    def __str__(self):
        return f"Image for Package {self.package.name}"


class Review(models.Model):
    package = models.ForeignKey(Package, related_name='reviews', on_delete=models.CASCADE)
    reviewer = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)
    review_text = models.TextField()
    rating = models.DecimalField(max_digits=2, decimal_places=1)

    def __str__(self):
        return f"Review by {self.reviewer.username} for {self.package.name}"
