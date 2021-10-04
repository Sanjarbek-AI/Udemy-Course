from django.contrib import admin

from updates.models import UpdateModel


@admin.register(UpdateModel)
class UpdateModelAdmin(admin.ModelAdmin):
    list_display = ['content', 'created_at', 'updated_at']
    search_fields = ['content']
    list_filter = ['created_at', 'updated_at']
