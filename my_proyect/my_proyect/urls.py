from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page),
    path('about/', views.about_page),

    path('post/', include('post.urls')),
    path('', include('users.urls')),

] 

urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)