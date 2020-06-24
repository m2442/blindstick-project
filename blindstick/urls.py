
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import gallary.views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', gallary.views.home, name='home'),
    path('about/', gallary.views.about, name='about'),
    path('blogs/', include('blogs.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
