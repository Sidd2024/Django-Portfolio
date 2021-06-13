from django.contrib import admin
from django.urls import path, include
from . import views
from .views import ContactCreate, thanks
from django.conf.urls.static import static
from home import views

# Django admin customization

admin.site.site_header = "Tech Lady Juwana"
admin.site.site_title = "Welcome to the Dashboard"
admin.site.index_title = "Welcome to the Admin Portal"
urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', views.blog, name='blog'),
    path('contact/', ContactCreate.as_view(), name='contact'),
    path('thanks/', thanks, name='thanks')
]
