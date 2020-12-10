from django.db import models


# Create your models here.
class Category(models.Model):
    Category = models.CharField(max_length=64, default='', blank=True, null=True)

    def __str__(self):
        return str(self.Category)


class Book(models.Model):
    Title = models.CharField(max_length=64, default='', blank=True, null=True)
    Category = models.ManyToManyField(Category)
    Year_of_publication = models.CharField(max_length=6, default='', blank=True, null=True)
    Writer = models.CharField(max_length=64, default='', blank=True, null=True)
    Price = models.FloatField(default=0.0, blank=True, null=True)
    Summary = models.TextField(max_length=1024, default='', blank=True, null=True)
    Cover = models.ImageField(upload_to='BookCovers/DefaultCover.jpg')
    Image_one = models.ImageField(upload_to='BookImages/DefaultImageOne', default='BookImages/DefaultImageOne.jpg')
    Image_two = models.ImageField(upload_to='BookImages/DefaultImageTwo', default='BookImages/DefaultImageTwo.jpg')

    def __str__(self):
        return '{}, {}, {}, {}'.format(self.Title, self.Category, self.Writer, str(self.Price),
                                       self.Year_of_publication)
