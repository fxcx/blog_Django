from django.contrib import admin
from django.urls import path, include
# #* Para subir imagenes
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page , name='index'),
    path('about/', views.about_page , name='about'),
    path('post/', include('post.urls')),
] 

urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)