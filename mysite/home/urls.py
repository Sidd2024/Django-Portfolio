from django.contrib import admin
from django.urls import path, include
from . import views
from .views import ContactCreate, thanks
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', views.blog, name='blog'),
    path('contact/', ContactCreate.as_view(), name='contact'),
    path('thanks/', thanks, name='thanks')
]
