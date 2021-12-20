
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views as reg_views
from django.views.generic import RedirectView
urlpatterns = [
    path('' , reg_views.home,name="home"),
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls')),
    path('teams/', include('teams.urls')),
    path('competitions/', include('competitions.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
