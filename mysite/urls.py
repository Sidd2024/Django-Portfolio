from django.contrib import admin
from django.urls import path, include
from home import views
# Add any of these imports if you don't already have them
from django.views.decorators.cache import cache_control
from django.contrib.staticfiles.views import serve
from django.conf.urls.static import static
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from django.conf.urls.defaults import patterns


# Add this after the rest of your urlpatterns. (Ensure you don't have another url defined for your static files
# urlpatterns += static(settings.STATIC_URL,
#                       view=cache_control(no_cache=True, must_revalidate=True)(serve))

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    #path('blog/', include('blog.urls')),

]

if not settings.DEBUG:
    #urlpatterns += static(settings.STATIC_URL)
    #urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT})
    )
