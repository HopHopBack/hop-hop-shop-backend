import os
import uuid

from django.db import models
from pytils.translit import slugify


def news_image_file_path(instance, filename):
    _, extension = os.path.splitext(filename)
    filename = f"{slugify(instance.title)}-{uuid.uuid4()}{extension}"
    return os.path.join("uploads/news_images/", filename)


class NewsType(models.TextChoices):
    HOTTEST = 'hottest', 'The Hottest'
    HIPHOP = 'choice', 'HopHop choice'
    LOVE = 'love', 'One Love'
    SECRET = 'secret', 'Customer Secret'
    DEFAULT = 'default', 'Default'


class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to=news_image_file_path, blank=True, null=True)
    type = models.CharField(max_length=20, choices=NewsType.choices, default=NewsType.DEFAULT)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created_at"]
