from django.db import models

# Create your models here.


# class Author(models.Model):
#     name = models.CharField(max_length=30)

#     def __str__(self):
#         return self.name


# class Category(models.Model):
#     name = models.CharField(max_length=20)

#     def __str__(self):
#         return self.name


# class Journal(models.Model):
#     title = models.CharField(max_length=120)
#     Author = models.ForeignKey(Author, on_delete=models.CASCADE)
#     categories = models.ManyToManyField(Category)
#     publish_date = models.DateTimeField(auto_now_add=True)
#     views = models.IntegerField(default=0)
#     reviewed = models.BooleanField(default=False)

#     def __str__(self):
#         return self.title


class Sentiment(models.Model):

    Product_Name = models.CharField(max_length=255)
    asin = models.CharField(max_length=50, blank=False)
    Positive = models.FloatField(max_length=50)
    Negative = models.FloatField(max_length=50)
    score = models.TextField()

    def __str__(self):
        return self.asin
