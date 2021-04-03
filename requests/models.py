from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class HTTPRequest(models.Model):
    content_type = models.CharField(max_length=100)
    encoding = models.CharField(max_length=10)

    connection = models.CharField(max_length=40)
    cache_control = models.CharField(max_length=40)
    accept_language = models.CharField(max_length=80)

    http_method = models.CharField(max_length=10)
    scheme = models.CharField(max_length=10)
    url = models.URLField()
    is_ajax = models.BooleanField()

    user_agent = models.CharField(max_length=300)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    load_time = models.FloatField()
