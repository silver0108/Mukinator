from django.db import models
from common.models import User


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    hit = models.PositiveIntegerField(default=0)
    category_Choices = (('서울','서울'), ('수원','수원'), ('용인','용인'),
                        ('부산','부산'), ('김해','김해'))
    region = models.CharField(max_length=10, choices=category_Choices)

    def __str__(self):
        return self.subject

    @property
    def update_counter(self):
        self.hit = self.hit + 1
        self.save()


class Photo(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
