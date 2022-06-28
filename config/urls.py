
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
app_name='accounts'
urlpatterns = [
    path('', include('core.urls', namespace='core')),
    path('rooms/',include('rooms.urls', namespace='rooms') ),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('users.urls', namespace='users')),
    path('blog/', include('blog.urls',namespace="blog")),
    path('admin/', admin.site.urls),
    
    
]

if settings.DEBUG:  # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
