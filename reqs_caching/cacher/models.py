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


class PartnerTestEnvironments(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    url = models.URLField()
    is_available = models.BooleanField(default=False)


class ProxyEmulatorSettings(models.Model):
    id = models.AutoField(primary_key=True)
    request_url = models.URLField()
    partner_test_environment = models.ForeignKey(PartnerTestEnvironments,
                                                 on_delete=models.CASCADE)
