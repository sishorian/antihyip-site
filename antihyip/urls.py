"""
URL configuration for antihyip project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # Admin site
    path("admin/", admin.site.urls),
    # hyiptest app
    path("", include("hyiptest.urls")),  # use root url for now
    # path("hyiptest/", include("hyiptest.urls")),
    # path("", RedirectView.as_view(url="hyiptest/", permanent=True)),
]

# Serve static files during development (only)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
