from model_utils.fields import MonitorField, StatusField
from model_utils import Choices

from django.db import models
from django.templatetags.static import static


class Article(models.Model):
    STATUS = Choices('draft', 'published')

    slug = models.CharField(max_length=54)
    title = models.CharField(max_length=128)
    subtitle = models.CharField(max_length=128, blank=True)
    image = models.ImageField(upload_to='img')
    teaser = models.TextField()
    content = models.TextField(blank=True)
    status = StatusField()
    published_at = MonitorField(monitor='status', when=['published'])


class Question(models.Model):
    STATUS = Choices('draft', 'published')

    slug = models.CharField(max_length=54)
    name = models.CharField(max_length=128)
    title = models.CharField(max_length=128, blank=True)
    subtitle = models.CharField(max_length=128, blank=True)
    main_image = models.ImageField(upload_to='img', blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    question = models.TextField()
    response = models.TextField(blank=True, null=True)
    status = StatusField()
    published_at = MonitorField(monitor='status', when=['published'])
