from rest_framework import serializers

from status.models import StatusModel


class StatusModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusModel
        fields = '__all__'
