"""
URL configuration for myassignment project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from movies.views import home, api_index  # Import the api_index view

urlpatterns = [
    path('', home, name='home'),  # Root URL
    path('admin/', admin.site.urls),
    path('api/', api_index, name='api-index'),  # Index response for /api/
    path('api/', include('movies.urls')),  # Include movies app's URLs
]
