"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from home import views
# Add any of these imports if you don't already have them
from django.views.decorators.cache import cache_control
from django.contrib.staticfiles.views import serve
from django.conf.urls.static import static
from . import settings
from django.core.mail import send_mail, BadHeaderError

# Add this after the rest of your urlpatterns. (Ensure you don't have another url defined for your static files
# urlpatterns += static(settings.STATIC_URL,
#                       view=cache_control(no_cache=True, must_revalidate=True)(serve))

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL)
    # urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
