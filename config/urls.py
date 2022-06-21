
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('', include('core.urls', namespace='core')),
    path('rooms/',include('rooms.urls', namespace='rooms') ),
    path('admin/', admin.site.urls),
    
    
]

if settings.DEBUG:  # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
