
from django.urls import path
from .views import EmailTokenObtainPairView, UserRegisterView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('token/', EmailTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', UserRegisterView.as_view(), name='user-register'),
]