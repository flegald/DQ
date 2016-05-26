# Puzzle book model.
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.conf import settings
from django.contrib.auth.models import User


@python_2_unicode_compatible
class Book(models.Model):
    """Book model."""

    title = models.CharField(default='', max_length=255)
    cover = models.ImageField(defaul='images/default.png')
    description = models.CharField(default='', max_length=255)
    price = models.CharField(default='', max_length=255)
