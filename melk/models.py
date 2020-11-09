from django.db import models
import datetime

class Amlak(models.Model):
    YEAR_CHOICE = []
    for i in range(1800, datetime.datetime.now().year+1):
        YEAR_CHOICE.append((i, i))

    TYPE_CHOICE = [
        ('r', 'Rahn'),
        ('e', 'Ejare'),
        ('f', 'Forush'),
    ]
    Title = models.CharField(max_length=100)
    Slug = models.SlugField()
    Metre = models.IntegerField()
    Description = models.TextField()
    Image = models.ImageField(default='default.jpg', blank=True)
    Year = models.IntegerField(choices=YEAR_CHOICE, default=datetime.datetime.now().year)
    Publish = models.DateTimeField(auto_now_add=True)
    Update = models.DateTimeField(auto_now=True)
    Type = models.CharField(max_length=1, choices=TYPE_CHOICE)

    def __str__(self):
        return self.Title

    def show(self):
        return self.Description[:40] +' ...'