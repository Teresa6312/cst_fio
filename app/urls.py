from django.contrib import admin
from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static
from django.views.i18n import JavaScriptCatalog

urlpatterns = [
    path('guanjia/', admin.site.urls),
    path('', include('base.urls', namespace='base')),
    path('_/', include('django.conf.urls.i18n')),
]

# js files translation
urlpatterns += (
    path('jsi18n/',
         JavaScriptCatalog.as_view(packages=['localejs.jscripti18n']),
         name='javascript-catalog'),
    
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

