from django.db import models


class Request(models.Model):
    url = models.CharField(max_length=255)
    method = models.CharField(max_length=10)
    headers = models.TextField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Response(models.Model):
    url = models.CharField(max_length=255)
    status_code = models.IntegerField()
    headers = models.TextField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
