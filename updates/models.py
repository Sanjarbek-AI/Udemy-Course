from django.conf import settings
from django.core.serializers import serialize
from django.db import models


class UpdateModel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='updates')
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to='updates')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content or " "

    def serialize(self):
        return serialize("json", UpdateModel)

    class Meta:
        verbose_name = 'update'
        verbose_name_plural = 'updates'
