from django.urls import path
from .views import CurrentUserDevicesView

urlpatterns = [
    path('my-devices/', CurrentUserDevicesView.as_view(), name='my-devices')
]