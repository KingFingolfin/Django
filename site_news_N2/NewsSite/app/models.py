from django.db import models


# Create your models here.

class OneTopic(models.Model):
    title = models.CharField(max_length=128)
    picture = models.ImageField(upload_to='images', default='images/default_picture.png', )
    text = models.TextField()
    nameAuthor = models.CharField(max_length=50, default='unknown')
    imageAuthor = models.ImageField(upload_to='images', default='images/default_author.jpg', )
    aboutAuthor = models.TextField(max_length=500, default="...")
    NEWS_TYPE = (
        ("1", "სხვა"),
        ("2", 'მეცნიერება'),
        ("3", 'პოლიტიკა'),
        ("4", 'ხელოვნება'),
        ("5", 'ისტორია'),
    )
    news_type = models.CharField(max_length=128, default="1", choices=NEWS_TYPE)

    def __str__(self):
        return self.title

    class Meta:  # gadawers
        verbose_name_plural = 'სტატიები'


class Ad(models.Model):
    title = models.CharField(max_length=128, default="unknown")
    image = models.ImageField(upload_to='images', default='images/template.png', )
    link = models.CharField(max_length=500, default="unknown")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'რეკლამა'


class Contact(models.Model):
    Name = models.CharField(max_length=20)
    Email = models.CharField(max_length=30)
    Phone = models.CharField(max_length=15)
    Subject = models.CharField(max_length=50)
    Message = models.TextField(max_length=500)

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name_plural = 'კონტაქტები'


class Gmails(models.Model):
    Email = models.CharField(max_length=30)

    def __str__(self):
        return self.Email

    class Meta:
        verbose_name_plural = 'მეილები'


class Comment(models.Model):
    article = models.ForeignKey(OneTopic, on_delete=models.CASCADE)
    username = models.CharField(max_length=20)
    text = models.TextField(max_length=1000)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = 'კომენტარები'
