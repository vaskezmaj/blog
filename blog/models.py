from django.db import models
from django.contrib.auth.models import User

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


# status tuple za render, kad je spreman za objavljivanje.


class Post(models.Model):
    naslov = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    update_on = models.DateTimeField(auto_now=True)
    sadrzaj = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)


class Meta:
    ordering = ['-created_on']
# klasa za objavljivanje novih postova na vrh


def __str__(self):
    return self.title
#citljiva forma za admina na primer

