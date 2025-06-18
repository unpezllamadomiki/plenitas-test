from rest_framework import generics, permissions

from .infrastructure.models import Device
from .serializers import DeviceSerializer

class CurrentUserDevicesView(generics.ListAPIView):
    serializer_class = DeviceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Device.objects.filter(user=self.request.user)