from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from django.urls import path
from django.views.generic.base import TemplateView


admin_str = 'Administración Omnibnk'
admin.site.site_header = admin_str
admin.site.site_title = admin_str

urlpatterns = [
    path('admin/', admin.site.urls),

    path(
        'robots.txt',
        TemplateView.as_view(template_name='robots.txt'),
    ),

    path(
        '',
        TemplateView.as_view(template_name='home.html'),
        name='home',
    ),

    path(
        'perfil/',
        include('user.urls_registration', namespace='registration')
    ),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
