from django.contrib import admin

from status.forms import StatusModelForm
from status.models import StatusModel


@admin.register(StatusModel)
class StatusModelAdmin(admin.ModelAdmin):
    form = StatusModelForm
    list_display = ['user', 'content', 'created_at', 'updated_at']
    search_fields = ['content']
    list_filter = ['created_at', 'updated_at']
