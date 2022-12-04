from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from App_post import views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('App_login.urls')),
    path('post/', include('App_post.urls')),
    path('', views.home, name='home'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
