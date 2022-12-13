from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('func_app/', include('app.urls')),
    path('calculator/', include('api.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
