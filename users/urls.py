from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView
from .views import (
    UserRegistrationView,
    CustomTokenObtainPairView,
    UserViewSet,
    UserStatsView
)

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    # Authentication endpoints
    path('auth/register/', UserRegistrationView.as_view(), name='user-register'),
    path('auth/login/', CustomTokenObtainPairView.as_view(), name='token-obtain-pair'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token-refresh'),

    # User management endpoints
    path('', include(router.urls)),

    # Statistics endpoint
    path('stats/', UserStatsView.as_view(), name='user-stats'),
]
