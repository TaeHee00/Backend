from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from gtd import settings


class Docs(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # 외래키 설정
    title = models.CharField(max_length=255, null=False)
    content = models.TextField(null=False)
    repository_url = models.CharField(max_length=1000, null=False)
    url = models.CharField(max_length=1000, null=True)
    language = models.CharField(max_length=30, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    is_deleted = models.BooleanField(default=False)