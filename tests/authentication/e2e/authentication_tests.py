import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APIClient

from apps.devices.infrastructure.models import Device

User = get_user_model()

@pytest.mark.django_db
class TestAuthentication:

    @pytest.fixture(autouse=True)
    def setup_method(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            email="testuser@example.com",
            password="strongpassword123"
        )

    def test_authentication_flow_success(self):

        # 2. Login with JWT
        url = reverse('token_obtain_pair')  # URL de simplejwt
        response = self.client.post(url, {
            "email": "testuser@example.com",
            "password": "strongpassword123"
        })

        assert response.status_code == 200
        assert "access" in response.data

        access_token = response.data["access"]

        # 3. Create example device
        Device.objects.create(user=self.user, name="Laptop", ip="192.168.1.1", is_active=True)

        # 4. Access to devices using user token
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token}")
        response = self.client.get(reverse('my-devices'))

        assert response.status_code == 200
        assert isinstance(response.data, list)
        assert any(d["name"] == "Laptop" for d in response.data)

    def test_authentication_invalid_user(self):
        client = APIClient()

        url = reverse('token_obtain_pair')
        response = client.post(url, {
            "email": "nonexistent@example.com",
            "password": "wrongpassword"
        }, format='json')

        assert response.status_code == 401

    def test_user_registration_success(self):
        url = reverse('user-register')

        data = {
            "email": "newuser@example.com",
            "password": "strongpassword123"
        }

        response = self.client.post(url, data, format='json')

        assert response.status_code == 201
        assert response.data == {"message": "User created successfully"}

        user_exists = User.objects.filter(email="newuser@example.com").exists()
        assert user_exists


