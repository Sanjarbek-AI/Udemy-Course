from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class StatusModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='status')
    content = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='status', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content[:50]

    class Meta:
        verbose_name = 'Status post'
        verbose_name_plural = 'Status posts'
