from django.contrib import admin
from django.urls import path, include
# Add any of these imports if you don't already have them
from django.views.decorators.cache import cache_control
#from django.contrib.staticfiles.views import serve
from django.contrib.staticfiles.storage import staticfiles_storage
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.base import RedirectView
from home import views



# Add this after the rest of your urlpatterns. (Ensure you don't have another url defined for your static files
# urlpatterns += static(settings.STATIC_URL,
#                       view=cache_control(no_cache=True, must_revalidate=True)(serve))

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    #path('blog/', include('blog.urls')),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('img/favicon.ico')))

]

if not settings.DEBUG:
    #urlpatterns += static(settings.STATIC_URL)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
