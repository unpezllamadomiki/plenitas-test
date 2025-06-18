from rest_framework import serializers
from apps.devices.infrastructure.models import Device


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ['id', 'name', 'ip', 'is_active']