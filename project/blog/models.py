from model_utils.fields import MonitorField, StatusField
from model_utils import Choices

from django.db import models
from django.templatetags.static import static


class Article(models.Model):
    STATUS = Choices('draft', 'published')

    title = models.CharField(max_length=128)
    subtitle = models.CharField(max_length=128)
    image = models.ImageField(upload_to='img')
    teaser = models.TextField()
    content = models.TextField()
    status = StatusField()
    published_at = MonitorField(monitor='status', when=['published'])
