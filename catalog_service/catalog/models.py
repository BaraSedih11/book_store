from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    price = models.FloatField()
    quantity = models.IntegerField()
    topic = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title

class Magazine(models.Model):
    title = models.CharField(max_length=255)
    price = models.FloatField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.title
