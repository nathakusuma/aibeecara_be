"""
URL configuration for aibeecara_be project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def api_root(request):
    """
    API Root endpoint with available routes
    """
    return Response({
        'message': 'Welcome to Django REST API',
        'endpoints': {
            'auth': {
                'register': '/api/auth/register/',
                'login': '/api/auth/login/',
                'refresh': '/api/auth/refresh/',
            },
            'users': {
                'list': '/api/users/',
                'detail': '/api/users/{id}/',
                'profile': '/api/users/profile/',
                'update_profile': '/api/users/update_profile/',
                'change_password': '/api/users/change_password/',
                'stats': '/api/stats/',
            }
        }
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api_root, name='api-root'),
    path('api/', include('users.urls')),
]